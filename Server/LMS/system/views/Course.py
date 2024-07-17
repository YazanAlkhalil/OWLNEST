# rest_framework
from rest_framework import generics, serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotAuthenticated, PermissionDenied
# models
from ..models.Course import Course
from ..models.Company import Company
from ..models.Admin_Contract import Admin_Contract
from ..models.Trainee_Contract import Trainee_Contract
from ..models.Trainee_Contract import Trainee_Contract
# serialzers
from ..serializers.Course import Course_Serializer
# permissions
from ..permissions.IsAdmin import IsAdmin
from ..permissions.IsCourseAdmin import IsCourseAdmin
from ..permissions.IsCourseAdminOrTrainer import IsCourseAdminOrTrainer
# swagger
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# GET : api/admin/company/:company-id/courses
# GET : api/trainer/company/:company-id/courses
# GET : api/trainee/company/:company-id/courses
class CompanyCourseList(generics.ListAPIView):
    # set the serializer class
    serializer_class = Course_Serializer
    # set the permission class
    permission_classes = [IsAuthenticated]
    # Document the view
    @swagger_auto_schema(
        operation_description="Retrieve a list of courses for a specific company",
        responses={200: Course_Serializer(many=True)}
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    # retrive the courses passed on the company id
    def get_queryset(self):
        company_id = self.kwargs['company_id']
        # get the user from the request body
        user = self.request.user
        # get the admin courses
        if user.is_admin:
            try:
                admin_contract = Admin_Contract.objects.get(admin=user.admin)
            except Admin_Contract.DoesNotExist:
                raise serializers.ValidationError("Admin contract does not exist for this user")
            return Course.objects.filter(id=company_id, admin_contract=admin_contract)
        # get the trainer courses
        elif user.is_trainer:
            try:
                trainer_contract = Trainee_Contract.objects.get(admin=user.trainer)
            except Trainee_Contract.DoesNotExist:
                raise serializers.ValidationError("Tranier contract does not exist for this user")
            return Course.objects.filter(id=company_id, trainer_contract=trainer_contract)
        # get the trainee courses
        elif user.is_trainee:
            try:
                trainee_contract = Trainee_Contract.objects.get(admin=user.trainee)
            except Trainee_Contract.DoesNotExist:
                raise serializers.ValidationError("Trainee contract does not exist for this user")
            return Course.objects.filter(enrollment__trainee_contract=trainee_contract, company=company_id)
    # when listing the courses set the view_type as list, otherwise set it as detail
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['view_type'] = 'list' if self.request.method == 'GET' else 'detail'
        return context

# POST: api/admin/company/:company-id/courses
class CompanyCourseCreate(generics.CreateAPIView):
    # set the serializer class
    serializer_class = Course_Serializer
    # set the permission class
    permission_classes = [IsAuthenticated, IsAdmin]
    # Document the view
    @swagger_auto_schema(
        operation_description="Create a new course for a specific company",
        request_body=Course_Serializer,
        responses={201: Course_Serializer}
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    # save the created company info
    def perform_create(self, serializer):
        user = self.request.user
        company_id = self.kwargs['company_id']
        try:
            company = Company.objects.get(id=company_id)
        except Company.DoesNotExist:
            raise serializers.ValidationError("Company does not exist")
        if user.is_admin:
            try:
                admin_contract = Admin_Contract.objects.get(admin=user.admin)
            except Admin_Contract.DoesNotExist:
                raise serializers.ValidationError("Admin contract does not exist for this user")
            serializer.save(company=company, admin_contract=admin_contract)
        else:
            raise serializer.ValidationError("Only admins can create courses")

# GET   : api/admin/company/:company-id/courses/course-id
# GET   : api/trainer/company/:company-id/courses/course-id
# GET   : api/trainee/company/:company-id/courses/course-id
class CompanyCourseRetrieve(generics.RetrieveAPIView):
    # set the serializer class
    serializer_class = Course_Serializer
    # set the permission class
    permission_classes = []
    # set the lookup field to match the URL keyword argument
    lookup_url_kwarg = 'course_id'
    # Document the view
    @swagger_auto_schema(
        operation_description="Retrieve a specific course from a specific company",
        responses={200: Course_Serializer(many=True)}
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    def get_queryset(self):    
        user = self.request.user
        company_id = self.kwargs['company_id']
        course_id = self.kwargs['course_id']
        # retrive the course if the admin is whom created it
        if user.is_admin:
            try:
                admin_contract = Admin_Contract.objects.get(admin=user.admin)
            except Admin_Contract.DoesNotExist:
                raise serializers.ValidationError("Admin contract does not exist for this user")
            return Course.objects.filter(id=course_id, admin_contract=admin_contract, company=company_id)
        # retrive the course if the trainer is whom created it
        elif user.is_trainer:
            try:
                trainer_contract = Trainee_Contract.objects.get(admin=user.trainer)
            except Trainee_Contract.DoesNotExist:
                raise serializers.ValidationError("Tranier contract does not exist for this user")            
            return Course.objects.filter(id=course_id, company=company_id, trainer_contract=trainer_contract)
        # retrive the course if the trainee has already enrolled in it 
        elif user.is_trainee:
            try:
                trainee_contract = Trainee_Contract.objects.get(admin=user.trainee)
            except Trainee_Contract.DoesNotExist:
                raise serializers.ValidationError("Trainee contract does not exist for this user")            
            return Course.objects.filter(id=course_id, enrollment__trainee_contract=trainee_contract, company=company_id)
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['view_type'] = 'detail'
        return context


# PUT   : api/admin/company/:company-id/courses/:course-id
# PUT   : api/trainer/company/:company-id/courses/:course-id
class CompanyCourseUpdate(generics.UpdateAPIView):
    # set the serializer class
    serializer_class = Course_Serializer
    # set the permission class
    permission_classes = [IsAuthenticated, IsCourseAdminOrTrainer]
    # set the lookup field to match the URL keyword argument
    lookup_url_kwarg = 'course_id'
    # Document the view
    @swagger_auto_schema(
        operation_description="update a specifice course from a specific company",
        request_body=Course_Serializer,
        responses={200: Course_Serializer}
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)
    def get_queryset(self):
        user = self.request.user
        company_id = self.kwargs['company_id']
        course_id = self.kwargs['course_id']
        # admin can edit only hiw courses
        if user.is_admin:
            try:
                admin_contract = Admin_Contract.objects.get(admin=user.admin)
            except Admin_Contract.DoesNotExist:
                raise serializers.ValidationError("Admin contract does not exist for this user")
            return Course.objects.filter(id=course_id, company=company_id, admin_contract=admin_contract)
        # trainer can edit only hiw courses
        elif user.is_trainer:
            try:
                trainer_contract = Trainee_Contract.objects.get(admin=user.trainer)
            except Trainee_Contract.DoesNotExist:
                raise serializers.ValidationError("Tranier contract does not exist for this user")            
            return Course.objects.filter(id=course_id, company=company_id, trainer_contract=trainer_contract)
        else:
            raise PermissionDenied("You do not have permission to edit courses")
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['view_type'] = 'detail'
        return context

# DELETE: api/admin/company/:company-id/courses/course-id
class CompanyCourseDelete(generics.DestroyAPIView):
    # set the serializer class
    serializer_class = Course_Serializer
    # set the permission class
    permission_classes = [IsAuthenticated, IsCourseAdmin]
    # set the lookup field to match the URL keyword argument
    lookup_url_kwarg = 'course_id'
    @swagger_auto_schema(
        operation_description="Delete a specific course for a specific company",
        responses={204: 'No Content'}
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
    def get_queryset(self):
        user = self.request.user
        company_id = self.kwargs['company_id']
        course_id = self.kwargs['course_id']
        # only admin can delete just the courses which he has created
        if user.is_admin:
            try:
                admin_contract = Admin_Contract.objects.get(admin=user.admin)
            except Admin_Contract.DoesNotExist:
                raise serializers.ValidationError("Admin contract does not exist for this user")
            return Course.objects.filter(id=course_id, company=company_id, admin_contract=admin_contract)
        else:
            raise PermissionDenied("You do not have permission to delete courses")
    def perform_destroy(self, instance):
        user = self.request.user
        if user.is_trainer or user.is_trainee:
            raise PermissionDenied("You do not have permission to delete courses")
        instance.delete()

# GET   : api/admin/company/:company-id/courses/course-id/info
# GET   : api/trainer/company/:company-id/courses/course-id/info
# GET   : api/trainee/company/:company-id/courses/course-id/info
class CompanyCourseRetriveInfo(generics.RetrieveAPIView):
    # set the serializer class
    serializer_class = Course_Serializer
    # set the permission class
    permission_classes = [IsAuthenticated]
    # set the lookup field to match the URL keyword argument
    lookup_url_kwarg = 'course_id'
    def get_queryset(self):    
        user = self.request.user
        company_id = self.kwargs['company_id']
        course_id = self.kwargs['course_id']
        # get the admin courses
        if user.is_admin:
            try:
                admin_contract = Admin_Contract.objects.get(admin=user.admin)
            except Admin_Contract.DoesNotExist:
                raise serializers.ValidationError("Admin contract does not exist for this user")
            return Course.objects.filter(id=course_id, company=company_id, admin_contract=admin_contract)
        # get the trainer courses
        elif user.is_trainer:
            try:
                trainer_contract = Trainee_Contract.objects.get(admin=user.trainer)
            except Trainee_Contract.DoesNotExist:
                raise serializers.ValidationError("Tranier contract does not exist for this user")            
            return Course.objects.filter(id=course_id, company=company_id, trainer_contract=trainer_contract)
        # get the trainee courses
        elif user.is_trainee:
            try:
                trainee_contract = Trainee_Contract.objects.get(admin=user.trainee)
            except Trainee_Contract.DoesNotExist:
                raise serializers.ValidationError("Trainee contract does not exist for this user")            
            return Course.objects.filter(id=course_id, enrollment__trainee_contract=trainee_contract, company=company_id)
        else:
            raise PermissionDenied("You do not have permission to view this course")
    # set the view_type to info (for sending all of the fields)
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['view_type'] = 'info'
        return context