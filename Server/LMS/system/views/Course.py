# rest_framework
from rest_framework import generics, serializers, permissions
from rest_framework.exceptions import NotAuthenticated, PermissionDenied
# models
from ..models.Course import Course
from ..models.Company import Company
# serialzers
from ..serializers.Course import Course_Serializer

# GET : api/admin/company/:company-id/courses
# GET : api/trainer/company/:company-id/courses
# GET : api/trainee/company/:company-id/courses
class CompanyCourseList(generics.ListAPIView):
    # set the serializer class
    serializer_class = Course_Serializer
    # set the permission class
    permission_classes = [permissions.IsAuthenticated]
    # retrive the courses passed on the company id
    def get_queryset(self):
        company_id = self.kwargs['company_id']
        # get the user from the request body
        user = self.request.user
        # check if the user us authenticated
        if not user.is_authenticated:
            raise NotAuthenticated("User is not authenticated")
        # get the admin courses
        if user.is_admin:
            admin_contract = user.admin.admin_contract
            return Course.objects.filter(Company=company_id, admin_contract=admin_contract)
        # get the trainer courses
        elif user.is_trainer:
            trainer_contract = user.trainer.trainer_contract
            return Course.objects.filter(Company=company_id, trainer_contract=trainer_contract)
        # get the trainee courses
        elif user.is_trainee:
            trainee_contract = user.trainee.trainee_contract
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
    permission_classes = [permissions.IsAuthenticated]
    # save the created company info
    def perform_create(self, serializer):
        user = self.request.user
        # check if the user us authenticated
        if not user.is_authenticated:
            raise NotAuthenticated("User is not authenticated")
        company_id = self.kwargs['company_id']
        try:
            company = Company.objects.get(id=company_id)
        except Company.DoesNotExist:
            raise serializers.ValidationError("Company does not exist")
        if user.is_admin:
            admin_contract = user.admin.admin_contract
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
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):    
        user = self.request.user
        company_id = self.kwargs['company_id']
        # check if the user us authenticated
        if not user.is_authenticated:
            raise NotAuthenticated("User is not authenticated")
        # retrive the course if the admin is whom created it
        if user.is_admin:
            return Course.objects.filter(company=company_id)
        # retrive the course if the trainer is whom created it
        elif user.is_trainer:
            trainer_contract = user.trainer.trainer_contract
            return Course.objects.filter(company=company_id, trainer_contract=trainer_contract)
        # retrive the course if the trainee has already enrolled in it 
        elif user.is_trainee:
            trainee_contract = user.trainee.trainee_contract
            return Course.objects.filter(enrollment__trainee_contract=trainee_contract, company=company_id)
    def get_object(self):
        queryset = self.get_queryset()
        course_id = self.kwargs['course_id']
        return generics.get_object_or_404(queryset, id=course_id)
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['view_type'] = 'detail'
        return context


# PUT   : api/admin/company/:company-id/courses/course-id
# PUT   : api/trainer/company/:company-id/courses/course-id
class CompanyCourseUpdate(generics.UpdateAPIView):
    # set the serializer class
    serializer_class = Course_Serializer
    # set the permission class
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        user = self.request.user
        company_id = self.kwargs['company_id']
        # check if the user us authenticated
        if not user.is_authenticated:
            raise NotAuthenticated("User is not authenticated")
        # admin can edit only hiw courses
        if user.is_admin:
            admin_contract = user.admin.admin_contract
            return Course.objects.filter(company=company_id, admin_contract=admin_contract)
        # trainer can edit only hiw courses
        elif user.is_trainer:
            trainer_contract = user.trainer.trainer_contract
            return Course.objects.filter(company=company_id, trainer_contract=trainer_contract)
        else:
            raise PermissionDenied("You do not have permission to edit courses")
    def get_object(self):
        queryset = self.get_queryset()
        course_id = self.kwargs['course_id']
        return generics.get_object_or_404(queryset, id=course_id)
    def perform_update(self, serializer):
        user = self.request.user
        if user.is_trainee:
            raise PermissionDenied("Trainees cannot edit courses")
        serializer.save()
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['view_type'] = 'detail'
        return context

# DELETE: api/company/:company-id/courses/course-id
class CompanyCourseDelete(generics.DestroyAPIView):
    # set the serializer class
    serializer_class = Course_Serializer
    # set the permission class
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        user = self.request.user
        company_id = self.kwargs['company_id']
        # check if the user us authenticated
        if not user.is_authenticated:
            raise NotAuthenticated("User is not authenticated")
        # only admin can delete just the courses which he has created
        if user.is_admin:
            admin_contract = user.admin.admin_contract
            return Course.objects.filter(company=company_id, admin_contract=admin_contract)
        else:
            raise PermissionDenied("You do not have permission to delete courses")
    def get_object(self):
        queryset = self.get_queryset()
        course_id = self.kwargs['course_id']
        return generics.get_object_or_404(queryset, id=course_id)
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
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):    
        user = self.request.user
        company_id = self.kwargs['company_id']
        # check if the user us authenticated
        if not user.is_authenticated:
            raise NotAuthenticated("User is not authenticated")
        # get the admin courses
        if user.is_admin:
            admin_contract = user.admin.admin_contract
            return Course.objects.filter(company=company_id, admin_contract=admin_contract)
        # get the trainer courses
        elif user.is_trainer:
            trainer_contract = user.trainer.trainer_contract
            return Course.objects.filter(company=company_id, trainer_contract=trainer_contract)
        # get the trainee courses
        elif user.is_trainee:
            trainee_contract = user.trainee.trainee_contract
            return Course.objects.filter(enrollment__trainee_contract=trainee_contract, company=company_id)
        else:
            raise PermissionDenied("You do not have permission to view this course")
    def get_object(self):
        queryset = self.get_queryset()
        course_id = self.kwargs['course_id']
        return generics.get_object_or_404(queryset, id=course_id)
    # set the view_type to info (for sending all of the fields)
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['view_type'] = 'info'
        return context