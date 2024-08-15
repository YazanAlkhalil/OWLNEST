#DRF imports 
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

#django 
from django.shortcuts import get_object_or_404

#serializers 
from system.serializers.CompanyMainDashboardSerializer import AdminMainDashboardSerializer

#models 
from system.models.Company import Company

class AdminMainDashboard(APIView): 
      permission_classes = [IsAuthenticated]
      def get(self,request,*args,**kwargs):
          company = get_object_or_404(Company,id = self.kwargs['id'])
          serialized_data = AdminMainDashboardSerializer(data = company)
          serialized_data.is_valid(raise_exception=True)
          return Response(serialized_data.data , status= status.HTTP_200_OK)
          
            