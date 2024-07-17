#DRF 
from rest_framework.views import APIView
from rest_framework.response import Response

#models 
from system.models.Trainee_Contract import Trainee_Contract 
from system.models.Enrollment import Enrollment
from system.models.Company import Company
from system.models.Favorite import Favorite

#serializers 
from system.serializers.FavoriteSerializer import FavoriteSerializer
#django  
from django.shortcuts import get_object_or_404



class AddToFavoriteView(APIView):
      
      def post(self,request,*args,**kwargs):
            company = get_object_or_404(Company,id = kwargs['id'])
            trainee_contract = get_object_or_404(Trainee_Contract ,trainee__user = request.user , company = company)
            enrollment = get_object_or_404(Enrollment, course__id = request.data.get('id'),trainee_contract = trainee_contract)
            data = { 
                  "enrollment":enrollment.id,
                  "trainee_contract":trainee_contract.id
            }
            favorite_serializer = FavoriteSerializer(data = data)
            favorite_serializer.is_valid(raise_exception = True)
            favorite_serializer.save()
            return Response(favorite_serializer.data, 201)

      def get(self, request, *args, **kwargs):
            company_id = kwargs.get('id')
            if not company_id:
                  return Response({"detail": "Company ID is required."}, status=400)
            company = get_object_or_404(Company, id=company_id)
            trainee_contracts = Trainee_Contract.objects.filter(trainee__user=request.user, company=company)
            favourites = Favorite.objects.filter(trainee_contract__in=trainee_contracts)
            favourites_serialized = FavoriteSerializer(favourites, many=True)
            return Response(favourites_serialized.data, 200)
