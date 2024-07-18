# rest_framework
from rest_framework import generics
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
from ..permissions.IsCourseAdminOrTrainer import IsCourseAdminOrTrainer
from ..permissions.IsCourseTrainer import IsCourseTrainer
# swagger
from drf_yasg.utils import swagger_auto_schema
from ..swagger.Unit import unit_retrive_list_response_body, unit_create_request_body, unit_create_respons_body

# GET : api/admin/company/:company_id/courses/:course_id/unit
# GET : api/trainer/company/:company_id/courses/:course_id/unit
class UnitList(generics.ListAPIView):
    # set the serializer class
    serializer_class = Unit_Serializer
    # set the permission class
    permission_classes = [IsAuthenticated, IsCourseAdminOrTrainer]
    # Document the view
    @swagger_auto_schema(
        operation_description='for presenting the list of courses for a specific company showing only the important data',
        responses={200: unit_retrive_list_response_body}
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
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
    # set the lookup field to match the URL keyword argument
    lookup_url_kwarg = 'unit_id'
    # Document the view
    @swagger_auto_schema(
        operation_description='for presenting a specific course from a specific company showing only the important data',
        responses={200: unit_retrive_list_response_body}
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
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
    # Document the view
    @swagger_auto_schema(
        operation_description='for creating a new unit to a specific course',
        request_body=unit_create_request_body,
        responses={200: unit_create_respons_body}
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    def perform_create(self, serializer):
        company_id = self.kwargs['company_id']
        course_id = self.kwargs['course_id']
        course = Course.objects.get(id=course_id, company__id=company_id)
        serializer.save(course=course, state='PR')

# PUT : api/trainer/company/:company_id/courses/:course_id/unit/:unit_id/update
class UnitUpdate(generics.UpdateAPIView):
    # set the serializer class
    serializer_class = Temp_Unit_Serializer
    # set the permission class
    permission_classes = [IsAuthenticated, IsCourseTrainer]
    # set the lookup field to match the URL keyword argument
    lookup_url_kwarg = 'unit_id'
    @swagger_auto_schema(
        operation_description='for updating a specific unit',
        responses={200: unit_retrive_list_response_body}
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)
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
    # set the lookup field to match the URL keyword argument
    lookup_url_kwarg = 'unit_id'
    # Document the endpoint
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