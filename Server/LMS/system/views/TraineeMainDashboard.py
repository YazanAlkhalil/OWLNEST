#DRF  
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

#django 
from django.shortcuts import get_object_or_404

#serializers 
from system.serializers.TraineeMainDashboard import TraineeMainDashboard

#models  
from system.models.Company import Company
from system.models.Trainee_Contract import Trainee_Contract
class TraineeMainDashboardView(APIView): 
      def get(self,request, *args, **kwargs):
            company = get_object_or_404(Company,id = kwargs['id'])
            trainee_contract = get_object_or_404(Trainee_Contract, trainee__user = request.user , company = company)
            dashboard_serializer = TraineeMainDashboard(data = {"trainee_contract" : trainee_contract})
            dashboard_serializer.is_valid(raise_exception=True)
            return Response(dashboard_serializer.data, status=status.HTTP_200_OK)