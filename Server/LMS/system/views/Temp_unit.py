# rest_framework
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
# models
from ..models.Temp_unit import Temp_Unit
from ..models.Course import Course
# serialzers
from ..serializers.Temp_Unit import Temp_Unit_Serializer
# permissions
from ..permissions.IsCourseTrainer import IsCourseTrainer
from ..permissions.IsCourseAdminOrTrainer import IsCourseAdminOrTrainer

# GET : api/admin/company/:company_id/courses/:course_id/unit/:unit_id/temp_unit
# GET : api/trainer/company/:company_id/courses/:course_id/unit/:unit_id/temp_unit
class TempUnitList(generics.ListAPIView):
    # set the serializer class
    serializer_class = Temp_Unit_Serializer
    # set the permission class
    permission_classes = [IsAuthenticated, IsCourseAdminOrTrainer]
    def get_queryset(self):
        company_id = self.kwargs['company_id']
        course_id = self.kwargs['course_id']
        unit_id = self.kwargs['unit_id']
        return Temp_Unit.objects.filter(unit=unit_id, course__id=course_id, course__company__id=company_id)

# GET : api/admin/company/:company_id/courses/:course_id/unit/:unit_id/temp_unit/pending
# GET : api/trainer/company/:company_id/courses/:course_id/unit/:unit_id/temp_unit/pending
class TempUnitListPending(generics.ListAPIView):
    # set the serializer class
    serializer_class = Temp_Unit_Serializer
    # set the permission class
    permission_classes = [IsAuthenticated, IsCourseAdminOrTrainer]
    def get_queryset(self):
        company_id = self.kwargs['company_id']
        course_id = self.kwargs['course_id']
        unit_id = self.kwargs['unit_id']
        return Temp_Unit.objects.filter(unit=unit_id, course__id=course_id, course__company__id=company_id, state='PE')

# POST : api/trainer/company/:company_id/courses/:course_id/temp_unit
class TempUnitCreate(generics.CreateAPIView):
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

# GET: api/admin/company/:company_id/courses/:course_id/temp_unit/:temp_unit_id
# GET: api/trainer/company/:company_id/courses/:course_id/temp_unit/:temp_unit_id
class TempUnitRetrieve(generics.RetrieveAPIView):
    # set the serializer class
    serializer_class = Temp_Unit_Serializer
    # set the permission class
    permission_classes = [IsAuthenticated, IsCourseAdminOrTrainer]
    def get_queryset(self):
        company_id = self.kwargs['company_id']
        course_id = self.kwargs['course_id']
        temp_unit_id = self.kwargs['temp_unit_id']
        return Temp_Unit.objects.filter(id=temp_unit_id, course__id=course_id, course__company__id=company_id)

# GET: api/trainer/company/:company_id/courses/:course_id/temp_unit/:temp_unit_id/publish
class TempUnitPublish(generics.UpdateAPIView):
    # set the serializer class
    serializer_class = Temp_Unit_Serializer
    # set the permission class
    permission_classes = [IsAuthenticated, IsCourseTrainer]
    def get_queryset(self):
        company_id = self.kwargs['company_id']
        course_id = self.kwargs['course_id']
        temp_unit_id = self.kwargs['temp_unit_id']
        return Temp_Unit.objects.filter(id=temp_unit_id, course__id=course_id, course__company__id=company_id)
    # set the state to Pending
    def perform_update(self, serializer):
        instance = serializer.save()
        instance.state = 'PE'
        instance.save()

# PUT: api/trainer/company/:company_id/courses/:course_id/temp_unit/:temp_unit_id
class TempUnitUpdate(generics.UpdateAPIView):
    # set the serializer class
    serializer_class = Temp_Unit_Serializer
    # set the permission class
    permission_classes = [IsAuthenticated, IsCourseTrainer]
    def get_queryset(self):
        company_id = self.kwargs['company_id']
        course_id = self.kwargs['course_id']
        temp_unit_id = self.kwargs['temp_unit_id']
        return Temp_Unit.objects.filter(id=temp_unit_id, course__id=course_id, course__company__id=company_id)
    # reset the state to the InProgress
    def perform_update(self, serializer):
        instance = serializer.save()
        instance.state = 'PR'
        instance.save()

# DELETE: api/trainer/company/:company_id/courses/:course_id/temp_unit/:temp_unit_id
class TempUnitDelete(generics.DestroyAPIView):
    # set the serializer class
    serializer_class = Temp_Unit_Serializer
    # set the permission class
    permission_classes = [IsAuthenticated, IsCourseTrainer]
    def get_queryset(self):
        company_id = self.kwargs['company_id']
        course_id = self.kwargs['course_id']
        temp_unit_id = self.kwargs['temp_unit_id']
        return Temp_Unit.objects.filter(id=temp_unit_id, course__id=course_id, course__company__id=company_id)