#DRF
from rest_framework.response import Response
from rest_framework.views import APIView
#models 
from system.models.DraftUnit import DraftUnit
from system.models.DraftContent import DraftContent


class ReorderCourseView(APIView):
      def post(self,request,*args,**kwargs):
          units = request.data["units"]
          for unit in units :
              obj = DraftUnit.objects.get(id=unit["id"])
              obj.order = unit["order"]
              obj.save()
              
              for content in unit["contents"]:
                  obj_content = DraftContent.objects.get(id=content["id"])
                  if obj_content.unit != obj:
                      obj_content.unit = obj 
                  obj_content.order = content["order"]
                  obj_content.save()
          return Response({"message": "Reordering and movement successful"})