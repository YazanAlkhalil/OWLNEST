#signals
from django.db.models.signals import post_save
from django.dispatch import receiver
#models 
from system.models.Finished_Content import Finished_Content
from system.models.Grade import Grade 
from system.models.Content import Content 
 
def calculate_progress(enrollment): 
      total_contents = Content.objects.filter(unit__course=enrollment.course).count()
      finished_contents = Finished_Content.objects.filter(enrollment=enrollment).count()
      submitted_tests = Grade.objects.filter(enrollment=enrollment).count()
      if total_contents > 0:
         total_finished = finished_contents + submitted_tests
         enrollment.progress = (total_finished / total_contents) * 100
      else:
          enrollment.progress = 0.0
          enrollment.save()


@receiver(post_save, sender=Finished_Content)
def update_progress_on_finished_content(sender, instance, created, **kwargs):
    if created:
        enrollment = instance.enrollment
        calculate_progress(enrollment)

@receiver(post_save, sender=Grade)
def update_progress_on_grade(sender, instance, created, **kwargs):
    if created:
        enrollment = instance.enrollment
        calculate_progress(enrollment)