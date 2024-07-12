#signals
from django.db.models.signals import post_save
from django.dispatch import receiver
#models 
from system.models.Finished_Content import Finished_Content
from system.models.Grade import Grade 
from system.models.Content import Content 

#utils 
from decimal import Decimal

 
def calculate_progress(enrollment): 
      total_contents = Content.objects.filter(unit__course=enrollment.course).count()
      finished_contents = Finished_Content.objects.filter(enrollment=enrollment).count()
      submitted_tests = Grade.objects.filter(enrollment=enrollment).count()
      #progress
      if total_contents > 0:
         total_finished = finished_contents + submitted_tests
         enrollment.progress = (total_finished / total_contents) * 100
      else:
          enrollment.progress = 0.0
      #xp 
      total_xp = 0 
      total_xp += finished_contents*10
      for grade in Grade.objects.filter(enrollment =enrollment):
            total_xp += grade.xp
      else:
           enrollment.xp_avg = 0.0
      if finished_contents > 0:
         course_full_xp = 0 
         '''
         video / pdf : xp = 10
         test : full_xp
         total = video /pdf + test
         '''
         for unit in enrollment.course.unit_set.all():
             for content in unit.content_set.all():
                 if content.is_video or content.is_pdf:
                     course_full_xp += 10
                 elif content.is_test : 
                     course_full_xp += Decimal(content.test_set.all().first().full_xp)
                 else : continue
         enrollment.xp_avg = (total_xp)/(course_full_xp) * 100
      enrollment.save()       




def generate_certification(enrollment):
    pass

@receiver(post_save, sender=Finished_Content)
def update_progress_on_finished_content(sender, instance, created, **kwargs):
    if created:
        enrollment = instance.enrollment
        calculate_progress(enrollment)
        #generate certification if passed
        
        

@receiver(post_save, sender=Grade)
def update_progress_on_grade(sender, instance, created, **kwargs):
    if created:
        enrollment = instance.enrollment
        calculate_progress(enrollment)
        #generate certification if passed
        