#DRF 
from rest_framework import serializers


#models  
from system.models.Finished_Content import Finished_Content
from system.models.Grade import Grade 
from system.models.Course import Course
from system.models.Unit import Unit
from system.models.Content import Content
 
#serializers 
from system.serializers.UnitSerializer import UnitSerializer
class CustomTraineeCourseDetailsSerializer(serializers.ModelSerializer):
        units = UnitSerializer(source = "unit_set",many = True,read_only = True)

        class Meta:
            model = Course 
            fields = ["id","name","units"]


        def to_representation(self, instance): 
          data = super().to_representation(instance) 
          enrollment = self.context.get('enrollment') 
          for unit in data.get('units', []):
              u = Unit.objects.get(id = unit["id"])
              is_unit_completed =  u.content_set.all().count() == (enrollment.finished_content_set.filter(content__unit = u).count() + enrollment.grade_set.filter(test__content__unit= u).count())
              unit['is_completed'] = is_unit_completed
              contents = unit.get('contents', [])
              for content in contents: 
                      content_id = content['id']
                      content_object = Content.objects.get(id = content_id)
                      if content_object.is_pdf or content_object.is_video:
                          is_content_completed = Finished_Content.objects.filter(
                              enrollment=enrollment,
                              content_id=content_id
                          ).exists()
                      
                          content['is_completed'] = is_content_completed 

                      if content_object.is_test: 
                           try:
                             grade =  Grade.objects.get(enrollment = enrollment , test__content__id = content_id) 
                             content['status'] = 1 if grade.score >= 60 else -1
                           except Grade.DoesNotExist:
                             content['status'] = 0
                    
          return data
