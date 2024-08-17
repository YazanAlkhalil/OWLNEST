#DRF
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
#models 
from system.models.Certificate import Certificate


class GetCertificationsView(APIView):
      permission_classes = [IsAuthenticated]
      def get(self,request,id):
          certifications = Certificate.objects.filter(trainee_contract__trainee__user = request.user,trainee_contract__company__id = id)
          response =[]
          for certificate in certifications:
               response.append({
                    "id":certificate.id,
                    "certificate":f"{certificate.certificate}"
               })

          return Response(response)