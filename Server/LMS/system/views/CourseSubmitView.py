#DRF
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError

#models 
from system.models.Course import Course
 
#serializers 
from system.serializers.AdminApprovmentSerializer import AdminApprovmentSerializer
from system.serializers.OwnerApprovmentsSerializer import OwnerApprovmentSerializer
#django 
from django.shortcuts import get_object_or_404






class CourseSubmitView(CreateAPIView):
      permission_classes = [IsAuthenticated]
      def post(self, request, *args, **kwargs):
          course = get_object_or_404(Course,id = kwargs["course_id"])
          print(type(course.company.owner ), type(course.creator))
          if course.company.owner == course.creator :
               if course in [app.course for app in course.creator.ownerapprovment_set.all()]:
                    return Response({"message":"The course is already submitted please wait Owner acception"},200)
               serialized_data = OwnerApprovmentSerializer(data = {"course":course.id,"owner":course.creator.id})
               serialized_data.is_valid(raise_exception=True)
               serialized_data.save()
               return Response({"message":"the course has been submitted to the owner"})


          if hasattr(course.creator , "admin") :
                admin_contract = course.creator  
                if course in [app.course for app in admin_contract.adminapprovment_set.all()]:
                    return Response({"message":"The course is already submitted please wait admin acception"},200)
                serialized_data = AdminApprovmentSerializer(data = {"course":course.id,"admin_contract":course.creator.id})
                serialized_data.is_valid(raise_exception=True)
                serialized_data.save()
          
          return Response({"message":"The course Submitted to the admin, Please wait approvment"},200)
