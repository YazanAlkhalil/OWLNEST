#DRF 
from rest_framework.views import APIView
from rest_framework.response import Response


#models 
from system.models.DraftUnit import DraftUnit

#django 
from django.shortcuts import get_object_or_404

class DeleteDraftUnitView(APIView):

      def delete(self,request,id):
          unit = get_object_or_404(DraftUnit , id = id)
          unit.delete()
          return Response({"message":"the unit deleted successfully"},204)