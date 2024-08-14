#DRF
from rest_framework import serializers   

#models 
from system.models.Course  import Course  

 
class EditCourseInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['name', 'pref_description',"image"]
 