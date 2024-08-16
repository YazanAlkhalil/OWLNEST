#signals
from django.db.models.signals import post_save , pre_delete,post_delete
from django.dispatch import receiver
#models 
from system.models.Finished_Content import Finished_Content
from system.models.Grade import Grade 
from system.models.Content import Content 
from system.models.Unit import Unit
from system.models.Content import Content
from system.models.Question import Question
 
 
# def calculate_progress(enrollment): 
#       total_contents = Content.objects.filter(unit__course=enrollment.course).count()
#       finished_contents = Finished_Content.objects.filter(enrollment=enrollment).count()
#       submitted_tests = Grade.objects.filter(enrollment=enrollment).count()
       
#       #progress
#       if total_contents > 0:
#          total_finished = finished_contents + submitted_tests
#          return (total_finished / total_contents) * 100
#       return 0
#       enrollment.save()    
#       #xp 
#       total_xp = 0 
#       total_xp += finished_contents*10
#       for grade in Grade.objects.filter(enrollment =enrollment):
#             total_xp += grade.xp
#       course_full_xp = 0 
#       for unit in enrollment.course.unit_set.all():
#           course_full_xp += ( 10 * unit.content_set.filter(is_test = False).count())+(100 *unit.content_set.filter(is_test = True).count())
#       if course_full_xp > 0 :
#          enrollment.xp_avg = (total_xp)/(course_full_xp) * 100
#       else :
#           enrollment.xp_avg = 0
#       enrollment.save()       


 

# @receiver(post_save, sender=Finished_Content)
# def update_progress_on_finished_content(sender, instance, created, **kwargs):
#     if created: 
#         enrollment = instance.enrollment
#         enrollment.progress = calculate_progress(enrollment)
#         enrollment.save()
#         #update trainee_contract xp 
#         enrollment.trainee_contract.total_xp += 10  
#         enrollment.trainee_contract.save()
#         calculate_progress(enrollment)
#         #generate certification if passed

#         enrollment.save()





















# @receiver(pre_delete, sender=Unit)
# def adjust_xp_on_delete(sender, instance, **kwargs):
#       course = instance.course 
#       for enrollment in course.enrollment_set.filter(trainee_contract__employed = True):
#           for content in enrollment.finished_content_set.all(): 
#               enrollment.trainee_contract.total_xp -= 10 
#               if enrollment.trainee_contract.total_xp >= 0 : 
#                 enrollment.trainee_contract.save()
#           for content in enrollment.grade_set.all():
#               enrollment.trainee_contract.total_xp -= content.xp
#               if enrollment.trainee_contract.total_xp >= 0 :
#                     enrollment.trainee_contract.save()
#           calculate_progress(enrollment) 


      

# @receiver(pre_delete, sender=Content)
# def adjust_xp_on_delete(sender, instance, **kwargs):
#       course = instance.unit.course 
#       for enrollment in course.enrollment_set.filter(trainee_contract__employed = True):
#           if instance in [ fin.content for fin in enrollment.finished_content_set.all()]: 
#                enrollment.trainee_contract.total_xp -= 10  
#                if enrollment.trainee_contract.total_xp >= 0 :
#                   enrollment.trainee_contract.save()
#           print(instance)
#           print(hasattr(instance,'test'))
#           if hasattr(instance,'test'):
#             print( instance.test.id)
#             print([ grade for grade in enrollment.grade_set.all()])
#             print()        
#           if hasattr(instance,'test') and instance.test.id in [ grade.test for grade in enrollment.grade_set.all()]  :
#                 enrollment.trainee_contract.total_xp -= enrollment.grade_set.get(test__content = instance).xp
#                 if enrollment.trainee_contract.total_xp >= 0 :
#                   enrollment.trainee_contract.save()
#           calculate_progress(enrollment) 

# @receiver(post_delete, sender=Unit)
# def adjust_xp_on_delete(sender, instance, **kwargs):
#       course = instance.course 
#       for enrollment in course.enrollment_set.filter(trainee_contract__employed = True):
#           calculate_progress(enrollment) 
#       if enrollment.progress != 100 :
#           enrollment.completed  = False

# @receiver(post_delete, sender=Content)
# def adjust_xp_on_delete(sender, instance, **kwargs):
#       course = instance.unit.course 
#       for enrollment in course.enrollment_set.filter(trainee_contract__employed = True):
#           calculate_progress(enrollment) 
#       if enrollment.progress != 100 :
#           enrollment.completed  = False











# from decimal import Decimal
# @receiver(post_save, sender=Grade)
# def update_progress_on_grade(sender, instance, created, **kwargs):
#     if created:
#         enrollment = instance.enrollment
#         calculate_progress(enrollment)
        
#         enrollment.trainee_contract.total_xp += Decimal(instance.xp)
#         enrollment.trainee_contract.save() 
#         calculate_progress(enrollment)


# @receiver(pre_delete,sender = Grade)
# def update_progress_on_deleted_grade(sender, instance, **kwargs):
#       instance.enrollment.trainee_contract.total_xp -= Decimal(instance.xp)
#       instance.enrollment.trainee_contract.save() 
#       calculate_progress(instance.enrollment)







# @receiver(post_save, sender=Question)
# def update_progress_on_grade(sender, instance, created, **kwargs):
#     if created:
#         test = instance.test
#         test.full_mark += instance.mark 
#         test.save()