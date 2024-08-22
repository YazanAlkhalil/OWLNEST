#DRF
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
 
#models 
from system.models.Company import Company
from system.models.Course import Course
from system.models.Notification import Notification

#serializers 
from system.serializers.CompanySerializer import CompanySerializer
#Django 
from django.db.models import Q



class GetUserCompaniesView(APIView):
      permission_classes = [IsAuthenticated]

      def get(self,request):
          user = request.user
          all_companies = Company.objects.filter(
              Q(admins__user=user) |
              Q(trainees__user=user) |
              Q(trainers__user=user) |
              Q(owner__user=user)
        ).distinct()
          
          serialized_companies =  CompanySerializer(all_companies,many =True,context = {"request":request})
          return Response({
              'username': user.username,
              'userImg': user.image.url,
              'companies': serialized_companies.data
          }, 200)