# rest_framework
from rest_framework import generics, serializers, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
# models
from ..models.Unit import Unit
from ..models.Temp_unit import Temp_Unit
from ..models.Course import Course
# serialzers
from ..serializers.Unit import Unit_Serializer
from ..serializers.Temp_Unit import Temp_Unit_Serializer
# permissions
from ..permissions.IsCourseAdmin import IsCourseAdmin
from ..permissions.IsCourseAdminOrTrainer import IsCourseAdminOrTrainer
from ..permissions.IsCourseTrainer import IsCourseTrainer
# swagger
from drf_yasg.utils import swagger_auto_schema

# GET : api/admin/company/:company_id/courses/:course_id/unit
# GET : api/trainer/company/:company_id/courses/:course_id/unit
class UnitList(generics.ListAPIView):
    # set the serializer class
    serializer_class = Unit_Serializer
    # set the permission class
    permission_classes = [IsAuthenticated, IsCourseAdminOrTrainer]
    def get_queryset(self):
        company_id = self.kwargs['company_id']
        course_id = self.kwargs['course_id']
        return Unit.objects.filter(course__id=course_id, course__company__id=company_id)

# GET: api/admin/company/:company_id/courses/:course_id/unit/:unit_id
# GET: api/trainer/company/:company_id/courses/:course_id/unit/:unit_id
class UnitRetrieve(generics.RetrieveAPIView):
    # set the serializer class
    serializer_class = Unit_Serializer
    # set the permission class
    permission_classes = [IsAuthenticated, IsCourseAdminOrTrainer]
    def get_queryset(self):
        company_id = self.kwargs['company_id']
        course_id = self.kwargs['course_id']
        unit_id = self.kwargs['unit_id']
        return Unit.objects.filter(id=unit_id, course__id=course_id, course__company__id=company_id)

# POST : api/trainer/company/:company_id/courses/:course_id/unit
class UnitCreate(generics.CreateAPIView):
    # set the serializer class
    serializer_class = Temp_Unit_Serializer
    # set the permission class
    permission_classes = [IsAuthenticated, IsCourseTrainer]
    # save the cours to the temp_unit
    def perform_create(self, serializer):
        company_id = self.kwargs['company_id']
        course_id = self.kwargs['course_id']
        course = Course.objects.get(id=course_id, company__id=company_id)
        serializer.save(course=course, state='PR')

# PUT : api/trainer/company/:company_id/courses/:course_id/unit/:unit_id
class UnitUpdate(generics.UpdateAPIView):
    # set the serializer class
    serializer_class = Temp_Unit_Serializer
    # set the permission class
    permission_classes = [IsAuthenticated, IsCourseTrainer]
    # @swagger_auto_schema(
    #     operation_description='for updating a specific unit',
    #     # responses={200: ''}
    # )
    # def put(self, request, *args, **kwargs):
    #     return super().delete(request, *args, **kwargs)
    def get_queryset(self):
        course_id = self.kwargs['course_id']
        unit_id = self.kwargs['unit_id']
        return Temp_Unit.objects.filter(id=unit_id, course=course_id)
    def perform_update(self, serializer):
        serializer.save(state='PR')

# DELETE : api/trainer/company/:company_id/courses/:course_id/unit/:unit_id
class UnitDelete(generics.DestroyAPIView):    # set the serializer class
    serializer_class = Temp_Unit_Serializer
    # set the permission class
    permission_classes = [IsAuthenticated, IsCourseTrainer]
    @swagger_auto_schema(
        operation_description='obviously for deleteing a specific unit',
        responses={200: 'Unit set to delete state'}
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
    def get_queryset(self):
        course_id = self.kwargs['course_id']
        unit_id = self.kwargs['unit_id']
        return Unit.objects.filter(id=unit_id, course=course_id)
    def perform_destroy(self, instance):
        instance.state = 'DE'
        return Response({'message':'Unit set to delete state'}, status=204)