# rest_framework
from django.http import Http404
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError
from django.shortcuts import get_object_or_404
# models
from ..models.Unit import Unit
from ..models.Temp_unit import Temp_Unit
from ..models.Course import Course
# serialzers
from ..serializers.Unit import Unit_Serializer
from ..serializers.Temp_Unit import Temp_Unit_Serializer
# permissions
from ..permissions.Trainer import IsTrainer, IsCompanyTrainer, IsCourseTrainer
# swagger
from drf_yasg.utils import swagger_auto_schema
from ..swagger.Unit import (
    unit_retrive_list_response_body, 
    unit_create_request_body, 
    unit_create_respons_body
)

#############################################################
#                                                           #
#                                                           #
#              UnAvailabel (just for testing purpose)       #
#                                                           #
#                                                           #
#############################################################

# GET : api/whatever/company/:company_id/courses/:course_id/unit
class UnitList(generics.ListAPIView):
    # set the serializer class
    serializer_class = Unit_Serializer
    # set the permission class
    permission_classes = [IsAuthenticated, ]
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
        try:
            units = Unit.objects.filter(course__id=course_id, course__company__id=company_id)
        except Unit.DoesNotExist:
            raise ValidationError('No units for this course')
        return units

# GET: api/whatever/company/:company_id/courses/:course_id/unit/:unit_id
class UnitRetrieve(generics.RetrieveAPIView):
    # set the serializer class
    serializer_class = Unit_Serializer
    # set the permission class
    permission_classes = [IsAuthenticated, ]
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
        try:
            unit =Unit.objects.filter(id=unit_id, course__id=course_id, course__company__id=company_id)
        except Unit.DoesNotExist:
            raise ValidationError('No such unit for this course')
        return unit


#############################################################
#                                                           #
#                                                           #
#                 Create Uint (Trainer Only)                #
#                                                           #
#                                                           #
#############################################################

# POST : api/trainer/company/:company_id/courses/:course_id/unit
class UnitCreate(generics.CreateAPIView):
    # set the serializer class
    serializer_class = Temp_Unit_Serializer
    # set the permission class
    permission_classes = [IsAuthenticated, IsTrainer, IsCompanyTrainer, IsCourseTrainer]
    # Document the view
    @swagger_auto_schema(
        operation_description='for creating a new unit to a specific course',
        request_body=unit_create_request_body,
        responses={200: unit_create_respons_body}
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    # save the cours to the temp_unit
    def perform_create(self, serializer):
        company_id = self.kwargs['company_id']
        course_id = self.kwargs['course_id']
        try:
            course = Course.objects.get(id=course_id, company__id=company_id)
        except Course.DoesNotExist:
            raise ValidationError({'message': 'Course does not exists'})
        serializer.save(course=course, state='PR')

#############################################################
#                                                           #
#                                                           #
#                  Update Unit (Trainer Only)               #
#                                                           #
#                                                           #
#############################################################

# PUT : api/trainer/company/:company_id/courses/:course_id/unit/:unit_id/update
class UnitUpdate(generics.UpdateAPIView):
    # set the serializer class
    serializer_class = Temp_Unit_Serializer
    # set the permission class
    permission_classes = [IsAuthenticated, IsTrainer, IsCompanyTrainer, IsCourseTrainer]
    # set the lookup field to match the URL keyword argument
    lookup_field = 'unit_id'
    # Document the view
    @swagger_auto_schema(
        operation_description='for updating a specific unit',
        responses={200: unit_retrive_list_response_body}
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)
    def get_queryset(self):
        course_id = self.kwargs['course_id']
        unit_id = self.kwargs['unit_id']
        try:
            temp_unit = Temp_Unit.objects.filter(id=unit_id, course=course_id)
        except Temp_Unit.DoesNotExist:
            raise ValidationError('No such temp_unit for this course')
        return temp_unit
    def perform_update(self, serializer):
        serializer.save(state='PR')

# DELETE : api/trainer/company/:company_id/courses/:course_id/unit/:unit_id/delete
class UnitDelete(generics.DestroyAPIView):    
    # set the serializer class
    serializer_class = Temp_Unit_Serializer
    # set the permission class
    permission_classes = [IsAuthenticated, IsTrainer, IsCompanyTrainer, IsCourseTrainer]
    # set the lookup field to match the URL keyword argument
    lookup_field = 'unit_id'
    # Document the endpoint
    @swagger_auto_schema(
        operation_description='obviously for deleteing a specific unit',
        responses={204}
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
    def get_queryset(self):
        course_id = self.kwargs['course_id']
        unit_id = self.kwargs['unit_id']
        unit = get_object_or_404(Unit, id=unit_id, course=course_id)
        if unit.published:
            temp_unit = get_object_or_404(Temp_Unit, unit=unit)
            return Temp_Unit.objects.filter(id=temp_unit.id)
        raise ValidationError({'message': f'Unit {unit} has not been published yet'})
    def perform_destroy(self, instance):
        instance.state = 'DE'
        instance.save()
        return Response({'message': f'{instance.title} in state Delete now, waiting for the approve to be deleted'}, status=status.HTTP_200_OK)

# PATCH: api/trainer/company/:company_id/courses/:course_id/unit/:unit_id/restore
class UnitRestore(generics.UpdateAPIView):    
    # set the serializer class
    serializer_class = Temp_Unit_Serializer
    # set the permission class
    permission_classes = [IsAuthenticated, IsTrainer, IsCompanyTrainer, IsCourseTrainer]
    # set the lookup field to match the URL keyword argument
    lookup_field = 'unit_id'
    # Document the endpoint
    @swagger_auto_schema(
        operation_description='obviously for restoring some deleted unit',
        responses={200: 'Unit set to InProgress state (restored)'}
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)
    def get_queryset(self):
        course_id = self.kwargs['course_id']
        unit_id = self.kwargs['unit_id']
        unit = get_object_or_404(Unit, id=unit_id, course=course_id)
        temp_unit = get_object_or_404(Temp_Unit, unit=unit)
        return Temp_Unit.objects.filter(id=temp_unit.id)
    def perform_update(self, serializer):
        temp_unit = serializer.instance
        temp_unit.state = 'PR'
        temp_unit.save()
        return Response({'message': f'resored {temp_unit.title} succesfully'}, status=status.HTTP_200_OK)

# DELETE : api/trainer/company/:company_id/courses/:course_id/unit/:unit_id/not_published/delete
class TempUnitDelete(generics.DestroyAPIView):
    # set the serializer class
    serializer_class = Temp_Unit_Serializer
    # set the permission class
    permission_classes = [IsAuthenticated, IsTrainer, IsCompanyTrainer, IsCourseTrainer]
    # set the lookup field to match the URL keyword argument
    lookup_url_kwarg = 'unit_id'
    lookup_field = 'id'
    # Document the endpoint
    @swagger_auto_schema(
        operation_description='obviously for deleteing a specific unit',
        responses={204}
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
    def get_queryset(self):
        course_id = self.kwargs['course_id']
        try:
            return Temp_Unit.objects.filter(course__id=course_id)
        except Temp_Unit.DoesNotExist:
            raise Http404({'message': "Temp_Unit not found"})
    def perform_destroy(self, instance):
        instance.delete()
        return Response({'message': f'Unit {instance.title} Deleted'}, status=status.HTTP_204_NO_CONTENT)