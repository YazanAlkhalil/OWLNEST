#signals
from django.db.models.signals import post_save ,post_delete
from django.dispatch import receiver
#models 
from system.models.Finished_Content import Finished_Content
from system.models.Grade import Grade 
from system.models.Content import Content  
from system.models.Content import Content
from system.models.Test import Test
 
 
def calculate_progress(enrollment): 
      total_contents = Content.objects.filter(unit__course=enrollment.course).count()
      finished_contents = Finished_Content.objects.filter(enrollment=enrollment).count()
      submitted_tests = Grade.objects.filter(enrollment=enrollment).count()
      test = Test.objects.filter(content__unit__course = enrollment.course).count()
      #progress
      if total_contents > 0:
         total_finished = finished_contents + submitted_tests
         enrollment.progress = (total_finished / total_contents) * 100
        

      #xp 
      finished_contents_xp = finished_contents*10 
      grades_xp = 0
      for grade in Grade.objects.filter(enrollment=enrollment) :
          if grade.score  >= 60 :
               grades_xp += 100 * grade.score 


      enrollment.xp_avg = (finished_contents_xp + grades_xp ) / (total_contents * 10 + test*100) * 100
      print(finished_contents,submitted_tests , enrollment.xp)
      enrollment.xp = finished_contents_xp + grades_xp
      enrollment.save()
 


def update_trainee_total_xp(trainee_contract):
    total = 0
    
    for enrollment in  trainee_contract.enrollment_set.all(): 
        total += enrollment.xp

    trainee_contract.total_xp = total
    trainee_contract.save()


@receiver(post_save, sender=Finished_Content)
def update_progress_on_finished_content(sender, instance, created, **kwargs):
    if created: 
        enrollment = instance.enrollment
        calculate_progress(enrollment)
        update_trainee_total_xp(enrollment.trainee_contract)



@receiver(post_delete, sender=Finished_Content)
def adjust_xp_on_delete(sender, instance, **kwargs):
      enrollment = instance.enrollment
      calculate_progress(enrollment)
      update_trainee_total_xp(enrollment.trainee_contract)


@receiver(post_save, sender=Grade)
def update_progress_on_grades(sender, instance, created, **kwargs):
    if created: 
        enrollment = instance.enrollment
        calculate_progress(enrollment)
        update_trainee_total_xp(enrollment.trainee_contract)






@receiver(post_delete, sender=Grade)
def adjust_xp_on_delete_grade(sender, instance, **kwargs):
      enrollment = instance.enrollment
      calculate_progress(enrollment)
      update_trainee_total_xp(enrollment.trainee_contract)






