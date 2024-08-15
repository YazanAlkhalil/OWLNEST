#DRF 
from rest_framework import serializers


#models  
from system.models.Finished_Content import Finished_Content
from system.models.Finished_Unit import Finished_Unit 
from system.models.Course import Course
 
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
              unit_id = unit['id'] 

              is_unit_completed = Finished_Unit.objects.filter(
                  enrollment=enrollment,
                  unit_id=unit_id
              ).exists()
              
              unit['is_completed'] = is_unit_completed
              contents = unit.get('contents', [])
              for content in contents:
                      content_id = content['id']
                       
                      is_content_completed = Finished_Content.objects.filter(
                          enrollment=enrollment,
                          content_id=content_id
                      ).exists()
                      
                      content['is_completed'] = is_content_completed
                      
                    
          
          return data
