#DRF
from rest_framework import serializers

#models 
from system.models.Course import Course
from system.models.Enrollment import Enrollment
from system.models.Trainer_Contract_Course import Trainer_Contract_Course

class TraineeCourseListSerializer(serializers.ModelSerializer):
      

      progress = serializers.SerializerMethodField()
      leader = serializers.SerializerMethodField()
      class Meta:
            model = Course
            fields = ["id","name","image","leader","progress"]

      def get_progress(self, obj): 
          user = self.context['request'].user 
          enrollment = Enrollment.objects.filter(
              trainee_contract__trainee__user=user,
              course=obj
          ).first()
          return enrollment.progress if enrollment else 0
      
      def get_leader(self, obj): 
        leader_contract = Trainer_Contract_Course.objects.filter(
            course=obj,
            is_leader=True
        ).select_related('trainer_contract__trainer__user').first()
 
        return leader_contract.trainer_contract.trainer.user.username if leader_contract else None