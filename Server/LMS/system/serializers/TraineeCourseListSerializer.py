#DRF
from rest_framework import serializers

#models 
from system.models.Course import Course
from system.models.Enrollment import Enrollment
from system.models.Trainer_Contract_Course import Trainer_Contract_Course
from system.models.Trainee_Contract import Trainee_Contract
from system.models.Favorite import Favorite


class TraineeCourseListSerializer(serializers.ModelSerializer):
      
      progress = serializers.SerializerMethodField() 
      is_favourite = serializers.SerializerMethodField()
      class Meta:
            model = Course
            fields = ["id","name","image","progress","is_favourite","rate"]

      def get_progress(self, obj): 
          user = self.context['request'].user 
          enrollment = Enrollment.objects.get(
              trainee_contract__trainee__user=user,
              course=obj
          ) 
          return enrollment.progress 
     
      def get_is_favourite(self, obj):
       
        user = self.context['request'].user
 
        trainee_contract = Trainee_Contract.objects.filter(
            trainee__user=user,
            employed=True
        ).first()
 
        enrollment = Enrollment.objects.filter(
            trainee_contract=trainee_contract,
            course=obj
        ).first()
 
        is_favourite = Favorite.objects.filter(
            trainee_contract=trainee_contract,
            enrollment=enrollment
        ).exists()

        return is_favourite