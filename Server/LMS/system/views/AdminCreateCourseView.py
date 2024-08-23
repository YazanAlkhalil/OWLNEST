#DRF 
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, status 
from rest_framework.response import Response  
from django.shortcuts import get_object_or_404
#models 
from system.models.Company  import Company  
from system.models.Admin import Admin
from system.models.Owner import Owner
from system.models.Admin_Contract import Admin_Contract
from django.contrib.contenttypes.models import ContentType



#serializer 
from system.serializers.CreateCourseSerializer import CreateCourseSerializer


#djngo 
from django.shortcuts import get_object_or_404

class AdminCreateCourseView(generics.CreateAPIView):

 
    permission_classes = [IsAuthenticated]

    def post(self, request, company_id): 
        company = get_object_or_404(Company, id=company_id)
        user = request.user
        #user is owner of the company 
        if company.owner.user == user:
            creator_model = Owner 
            creator_content_type = ContentType.objects.get_for_model(creator_model)
            creator_instance = get_object_or_404(creator_model, user =request.user)
          
            serializer = CreateCourseSerializer(data=request.data)
            serializer.is_valid(raise_exception= True) 
            serializer.save(company=company, creator_content_type=creator_content_type,creator_object_id=creator_instance.id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            
           
        if hasattr(request.user, 'admin'):
            creator_model = Admin_Contract 
            creator_content_type = ContentType.objects.get_for_model(creator_model)
            creator_instance ,_= creator_model.objects.get_or_create(admin__user=request.user)


            serializer = CreateCourseSerializer(data=request.data)
            serializer.is_valid(raise_exception= True) 
            serializer.save(company=company, creator_content_type=creator_content_type,creator_object_id=creator_instance.id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            