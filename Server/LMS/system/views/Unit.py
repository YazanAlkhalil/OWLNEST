# rest_framework
from rest_framework import generics, serializers, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
# models
from ..models.Unit import Unit
from ..models.Temp_unit import Temp_Unit
# serialzers
from ..serializers.Unit import Unit_Serializer
# permissions
from ..permissions.IsCourseAdmin import IsCourseAdmin
from ..permissions.IsCourseAdminOrTrainer import IsCourseAdminOrTrainer

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

# POST : api/admin/company/:company_id/courses/:course_id/temp_unit/:temp_unit_id/approve
class UnitCreate(generics.CreateAPIView):
    # set the serializer class
    serializer_class = Unit_Serializer
    # set the permission class
    permission_classes = [IsAuthenticated, IsCourseAdmin]
    # save the cours to the temp_unit 
    def perform_create(self, serializer):
        company_id = self.kwargs['company_id']
        course_id = self.kwargs['course_id']
        temp_unit_id = self.kwargs['temp_unit_id']
        try:
            temp_unit = Temp_Unit.objects.get(id=temp_unit_id, course__id=course_id, course__company__id=company_id)
        except Temp_Unit.DoesNotExist:
            raise serializers.ValidationError("Temp_unit does not exist")
        if temp_unit.state != 'PE':
            raise serializers.ValidationError("Temp_unit is not in the pending state")
        # Create and save the Unit instance
        unit = Unit(
            course=temp_unit.course,
            title=temp_unit.title,
            pref_description=temp_unit.pref_description,
            order=temp_unit.order
        )
        unit.save()
        # Update the state of the Temp_Unit instance and set the unit to it
        temp_unit.state = 'PU'
        temp_unit.unit = unit
        temp_unit.save()
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response(response.data, status=status.HTTP_201_CREATED)