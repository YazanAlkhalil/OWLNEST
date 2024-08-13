#DRF 
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, status 
from rest_framework.response import Response  
from django.shortcuts import get_object_or_404
#models 
from system.models.Company  import Company  




#serializer 
from system.serializers.CreateCourseSerializer import CreateCourseSerializer


#djngo 
from django.shortcuts import get_object_or_404

class AdminCreateCourseView(generics.CreateAPIView):

 
    permission_classes = [IsAuthenticated]

    def post(self, request, company_id): 
        company = get_object_or_404(Company, id=company_id)
 
        if hasattr(request.user, 'admin'):
            admin_contract = request.user.admin.admin_contract_set.get(company = company_id)
        else:
            return Response({"error": "User does not have admin privileges in this company."}, status=status.HTTP_403_FORBIDDEN)
 
        serializer = CreateCourseSerializer(data=request.data)
        if serializer.is_valid(): 
            serializer.save(company=company, admin_contract=admin_contract)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

 