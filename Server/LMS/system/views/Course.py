# rest_framework
from rest_framework import generics, serializers, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
# models
from ..models.Course import Course
from ..models.Company import Company
from ..models.Admin_Contract import Admin_Contract
from ..models.Trainee_Contract import Trainee_Contract
from ..models.Trainer_Contract import Trainer_Contract
from ..models.Temp_unit import Temp_Unit
from ..models.Temp_Content import Temp_Content
from ..models.Unit import Unit
from ..models.Content import Content
from ..models.Pdf import Pdf
from ..models.Video import Video
from ..models.Test import Test
# serialzers
from ..serializers.Course import Course_Serializer
# permissions
from ..permissions.IsAdmin import IsAdmin
from ..permissions.IsCourseAdmin import IsCourseAdmin
from ..permissions.IsCourseAdminOrTrainer import IsCourseAdminOrTrainer
from ..permissions.IsCourseTrainer import IsCourseTrainer
# swagger
from drf_yasg.utils import swagger_auto_schema
from ..swagger.Course import course_create_request_body, course_list_response_body, course_retrive_response_body, course_retrive_info_response_body, course_delete_response_body, course_publish_approve_request_body

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
        operation_description='for presenting the list of courses for a specific company showing only the important data \'name and the image\' of the course',
        responses={200: course_list_response_body}
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
            return Course.objects.filter(company_id=company_id, admin_contract=admin_contract)
        # get the trainer courses
        elif user.is_trainer:
            try:
                trainer_contract = Trainer_Contract.objects.get(trainer=user.trainer)
            except Trainer_Contract.DoesNotExist:
                raise serializers.ValidationError("Tranier contract does not exist for this user")
            return Course.objects.filter(company_id=company_id, trainer_contract_course__trainer_contract=trainer_contract)
        # get the trainee courses
        elif user.is_trainee:
            try:
                trainee_contract = Trainee_Contract.objects.get(trainee=user.trainee)
            except Trainee_Contract.DoesNotExist:
                raise serializers.ValidationError("Trainee contract does not exist for this user")
            return Course.objects.filter(enrollment__Trainee_Contract=trainee_contract, company=company_id)
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
        operation_description='for creating a new course at least should have the following required fields',
        request_body=course_create_request_body,
        responses={201: course_retrive_response_body}
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

# POST: api/trainer/company/:company_id/courses/:course_id/publish
class CompanyCoursePublish(generics.UpdateAPIView):
    # set the serializer class
    serializer_class = Course_Serializer
    # set the permission class
    permission_classes = [IsAuthenticated, IsCourseTrainer]
    @swagger_auto_schema(
        operation_description='Publish a specific course with all its units and contents',
        request_body=course_publish_approve_request_body,
        responses={200: 'Published'}
    )
    def post(self, request, *args, **kwargs):
        company_id = self.kwargs['company_id']
        course_id = self.kwargs['course_id']
        course = Course.objects.get(id=course_id, company_id=company_id)
        course.state = 'PE'
        course.save()
        temp_units = Temp_Unit.objects.filter(course=course_id)
        for temp_unit in temp_units:
            temp_unit.state = 'PE'
            temp_unit.save()
            temp_contents = Temp_Content.objects.filter(temp_unit=temp_unit)
            for temp_content in temp_contents:
                temp_content.state = 'PE'
                temp_content.save()
        return Response({'status': 'Published'}, status=status.HTTP_200_OK)

# POST: api/admin/company/:company_id/courses/:course_id/approve
class CompanyCourseApprove(generics.CreateAPIView):
    # set the serializer class
    serializer_class = Course_Serializer
    # set the permission class
    permission_classes = [IsAuthenticated, IsCourseAdmin]
    @swagger_auto_schema(
        operation_description='Approve a specific course with all its units and contents',
        request_body=course_publish_approve_request_body,
        responses={200: 'Approved'}
    )
    def post(self, request, *args, **kwargs):
        company_id = self.kwargs['company_id']
        course_id = self.kwargs['course_id']
        course = Course.objects.get(id=course_id, company_id=company_id)
        # Check if all units and contents are in 'PE' state
        temp_units = Temp_Unit.objects.filter(course=course_id)
        if not temp_units.exists():
            return Response({'error': 'No units in pending or delete state'}, status=status.HTTP_400_BAD_REQUEST)
        # check if the contetnt of each unit is in 'PE' state
        for temp_unit in temp_units:
            temp_contents = Temp_Content.objects.filter(temp_unit=temp_unit)
            # delete the old unit
            if temp_unit.unit:
                Unit.objects.get(id=temp_unit.unit).delete()
            # if unit in state delete then delete it from the temp_unit
            if temp_unit.state == 'DE':
                temp_unit.delete()
                for temp_content in temp_contents:
                    # delete the old content
                    if temp_content.content:
                        Content.objects.get(id=temp_content.content).delete()
                    # if content in delete then delete it from the temp_content
                    if temp_content.state == 'DE':
                        temp_content.delete()
            elif temp_unit.state == 'PE':
                # Move Temp_Unit to Unit and mark it as 'PU'
                unit = Unit.objects.create(
                    course=course,
                    title=temp_unit.title,
                    order=temp_unit.order
                )
                temp_unit.unit = unit
                temp_unit.state = 'PU'
                temp_unit.save()
                for temp_content in temp_contents:
                    # delete the old content
                    if temp_content.content:
                        Content.objects.get(id=temp_content.content).delete()
                    # if content in delete then delete it from the temp_content
                    if temp_content.state == 'DE':
                        temp_content.delete()
                    elif temp_content.state == 'PE':
                        # Move Temp_Content to Content and mark them as 'PU'
                        content = Content.objects.create(
                            unit=unit,
                            title=temp_content.title,
                            order=temp_content.order,
                            is_video=temp_content.is_video,
                            is_pdf=temp_content.is_pdf,
                            is_test=temp_content.is_test
                        )
                        temp_content.content = content
                        temp_content.state = 'PU'
                        temp_content.save()
                        # Move specific content type (Pdf, Video, Test) to access it from the content table
                        if temp_content.is_pdf:
                            pdf = Pdf.objects.get(temp_content=temp_content)
                            pdf.content = content
                            pdf.temp_content = None
                            pdf.save()
                        elif temp_content.is_video:
                            video = Video.objects.get(temp_content=temp_content)
                            video.content = content
                            video.temp_content = None
                            video.save()
                        elif temp_content.is_test:
                            video = Video.objects.get(temp_content=temp_content)
                            video.content = content
                            video.temp_content = None
                            video.save()
                        elif temp_content.is_test:
                            test = Test.objects.get(temp_content=temp_content)
                            test.content = content
                            test.temp_content = None
                            test.save()
        # change the course state to 'PU'
        course.state = 'PU'
        course.save()
        return Response({'status': 'Approved'}, status=status.HTTP_200_OK)

# GET   : api/admin/company/:company-id/courses/course-id
# GET   : api/trainer/company/:company-id/courses/course-id
# GET   : api/trainee/company/:company-id/courses/course-id
class CompanyCourseRetrieve(generics.RetrieveAPIView):
    # set the serializer class
    serializer_class = Course_Serializer
    # set the permission class
    permission_classes = [IsAuthenticated]
    # set the lookup field to match the URL keyword argument
    lookup_url_kwarg = 'course_id'
    # Document the view
    @swagger_auto_schema(
        operation_description='for presenting a specific course details (all the main course data) \nNote: that this is not for the info page which present the whole information about the course and the additional resources',
        responses={200: course_retrive_response_body}
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
                trainer_contract = Trainer_Contract.objects.get(trainer=user.trainer)
            except Trainer_Contract.DoesNotExist:
                raise serializers.ValidationError("Tranier contract does not exist for this user")            
            return Course.objects.filter(id=course_id, company=company_id, trainer_contract_course__trainer_contract=trainer_contract)
        # retrive the course if the trainee has already enrolled in it 
        elif user.is_trainee:
            try:
                trainee_contract = Trainee_Contract.objects.get(trainee=user.trainee)
            except Trainee_Contract.DoesNotExist:
                raise serializers.ValidationError("Trainee contract does not exist for this user")            
            return Course.objects.filter(id=course_id, enrollment__Trainer_Contract=trainee_contract, company=company_id)
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['view_type'] = 'detail'
        return context


# GET   : api/admin/company/:company-id/pending_courses/course-id
class CompanyCourseRetrievePending(generics.RetrieveAPIView):
    # set the serializer class
    serializer_class = Course_Serializer
    # set the permission class
    permission_classes = [IsAuthenticated]
    # set the lookup field to match the URL keyword argument
    lookup_url_kwarg = 'course_id'
    # Document the view
    @swagger_auto_schema(
        operation_description='for presenting a specific pended course details (all the main course data)',
        responses={200: course_retrive_response_body}
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
            course = Course.objects.filter(id=course_id, admin_contract=admin_contract, company=company_id)
            for unit in Temp_Unit.objects.filter(course=course[0]):
                if unit.state == 'PE':
                    return course
                for content in Temp_Content.objects.filter(temp_unit=unit):
                    if content.state == 'PE':
                        return course
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
        operation_description='for presenting a specific course details (all the main course data) \nNote: that this is not for the info page which present the whole information about the course and the additional resources',
        request_body=Course_Serializer,
        responses={200: course_retrive_response_body}
    )
    def put(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)
    def get_queryset(self):
        user = self.request.user
        company_id = self.kwargs['company_id']
        course_id = self.kwargs['course_id']
        # admin can edit only his courses
        if user.is_admin:
            try:
                admin_contract = Admin_Contract.objects.get(admin=user.admin)
            except Admin_Contract.DoesNotExist:
                raise serializers.ValidationError("Admin contract does not exist for this user")
            return Course.objects.filter(id=course_id, company=company_id, admin_contract=admin_contract)
        # trainer can edit only his courses
        elif user.is_trainer:
            try:
                trainer_contract = Trainer_Contract.objects.get(trainer=user.trainer)
            except Trainer_Contract.DoesNotExist:
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
        operation_description='obviously for deleteing a specific course',
        responses={204: course_delete_response_body}
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
        return Response({'message':'Course Deleted'}, status=204)

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
    # Document the view
    @swagger_auto_schema(
        operation_description="Retrieve a specific course whole information from a specific company for the extra page with the additional info and stuff",
        responses={200: course_retrive_info_response_body}
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
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
                trainer_contract = Trainer_Contract.objects.get(trainer=user.trainer)
            except Trainer_Contract.DoesNotExist:
                raise serializers.ValidationError("Tranier contract does not exist for this user")            
            return Course.objects.filter(id=course_id, company=company_id, trainer_contract=trainer_contract)
        # get the trainee courses
        elif user.is_trainee:
            try:
                trainee_contract = Trainee_Contract.objects.get(trainee=user.trainee)
            except Trainee_Contract.DoesNotExist:
                raise serializers.ValidationError("Trainee contract does not exist for this user")            
            return Course.objects.filter(id=course_id, enrollment__Trainer_Contract=trainee_contract, company=company_id)
        else:
            raise PermissionDenied("You do not have permission to view this course")
    # set the view_type to info (for sending all of the fields)
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['view_type'] = 'info'
        return context