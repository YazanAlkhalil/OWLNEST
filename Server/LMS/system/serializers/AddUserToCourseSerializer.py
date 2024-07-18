#DRF
from rest_framework.serializers import ModelSerializer
from rest_framework.validators import ValidationError

#models
from system.models.Course import Course
from system.models.Trainee_Contract import Trainee_Contract
from system.models.Trainer_Contract_Course import Trainer_Contract_Course
from system.models.Enrollment import Enrollment
from system.models.Trainer_Contract import Trainer_Contract 

class AddTraineeToCourseSerializer(ModelSerializer):

      class Meta:
            model = Enrollment
            fields = ["id","course","trainee_contract"]
            extra_kwargs = {
                  "course":{'read_only':True}
                  ,"trainee_contract":{'read_only':True}
            }
      def to_internal_value(self, data):
            trainee_contract=  data["trainee_contract"]
            course = data["course"]
            data = super().to_internal_value(data)
            data["trainee_contract"]= trainee_contract
            data["course"]= course
            return data
 

class AddTrainerToCourseSerializer(ModelSerializer):
        class Meta:
            model = Trainer_Contract_Course
            fields = ["id","course","trainer_contract"]
