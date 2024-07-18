#DRF 
from rest_framework.serializers  import ModelSerializer

#models 
from system.models.Trainee_Contract import Trainee_Contract
class TraineeContractSerializer(ModelSerializer):
      class Meta:
            model = Trainee_Contract
            fields = '__all__'