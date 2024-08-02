# datetime
from datetime import date
# rest_framework
from rest_framework.exceptions import ValidationError
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
# django
from django.db import transaction
from django.db.models import F, Exists, OuterRef
# models
from ..models.Course import Course
from ..models.Company import Company
from ..models.Admin_Contract import Admin_Contract
from ..models.Trainee_Contract import Trainee_Contract
from ..models.Trainer_Contract import Trainer_Contract
from ..models.Trainer_Contract_Course import Trainer_Contract_Course
from ..models.Temp_unit import Temp_Unit
from ..models.Temp_Content import Temp_Content
from ..models.Unit import Unit
from ..models.Content import Content
from ..models.Pdf import Pdf
from ..models.Video import Video
from ..models.Test import Test
from ..models.Favorite import Favorite
# serialzers
from ..serializers.Course import Course_Serializer
from ..serializers.Course_Pending import Course_Pending_Progress_Serializer
from ..serializers.User_Result import User_Result_Serializer
from ..serializers.Trainer_Contract_Course_Leader import Trainer_Contract_Course_Leader_Serializer
# permissions
from ..permissions.IsCourseAdmin import IsCourseAdmin
from ..permissions.IsCourseAdminOrTrainer import IsCourseAdminOrTrainer
from ..permissions.IsCourseTrainer import IsCourseTrainer
from ..permissions.IsAdmin import IsAdmin
from ..permissions.IsOwnerOrAdminForCourse import IsOwnerOrAdminForCourse
# swagger
from drf_yasg.utils import swagger_auto_schema
from ..swagger.Course import course_create_request_body, course_list_response_body, course_retrive_response_body, course_retrive_info_response_body, course_delete_response_body, course_publish_approve_request_body





#v2 imports 
#serializers
from system.serializers.AdminCourseListSerializer import AdminCourseListSerializer
from system.serializers.TrainerCourseListSerializer import TrainerCourseListSerializer
from system.serializers.TraineeCourseListSerializer import TraineeCourseListSerializer
#permissions
from system.permissions.IsAdmin import IsCompanyOwner,IsAdminInCompany ,IsAdminInCompanyOrOwner




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
                admin_contract = Admin_Contract.objects.get(admin=user.admin, company__id=company_id, employed=True)
            except Admin_Contract.DoesNotExist:
                raise ValidationError("Admin contract does not exist for this user")
            try:
                courses = Course.objects.filter(company_id=company_id, admin_contract=admin_contract)
            except Course.DoesNotExist:
                raise ValidationError('No courses for this admin in this company')
            return courses
        # get the trainer courses
        elif user.is_trainer:
            try:
                trainer_contract = Trainer_Contract.objects.get(trainer=user.trainer, company__id=company_id, employed=True)
            except Trainer_Contract.DoesNotExist:
                raise ValidationError("Tranier contract does not exist for this user")
            try:
                courses = Course.objects.filter(company_id=company_id, trainer_contract_course__trainer_contract=trainer_contract)
            except Course.DoesNotExist:
                raise ValidationError('No courses for this trainer in this company')
            return courses
        # get the trainee courses
        elif user.is_trainee:
            try:
                trainee_contract = Trainee_Contract.objects.get(trainee=user.trainee, company__id=company_id, employed=True)
            except Trainee_Contract.DoesNotExist:
                raise ValidationError("Trainee contract does not exist for this user")
            try:
                courses = Course.objects.filter(enrollment__trainee_contract=trainee_contract, company=company_id).annotate(
                    progress=F('enrollment__progress'),
                    is_favorite=Exists(Favorite.objects.filter(enrollment__course=OuterRef('pk'), trainee_contract=trainee_contract))
                )
            except Course.DoesNotExist:
                raise ValidationError('No courses for this trainee in this company')
            return courses
        elif user.is_owner:
            try:
                courses = Course.objects.filter(company__owner=user.owner)
            except Course.DoesNotExist:
                raise ValidationError('No courses for this owner in this company')
            return courses
        else:
            return Response({'message': 'No Content'}, status=status.HTTP_204_NO_CONTENT)
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
            raise ValidationError("Company does not exist")
        if user.is_admin:
            try:
                admin_contract = Admin_Contract.objects.get(admin=user.admin, company__id=company_id, employed=True)
            except Admin_Contract.DoesNotExist:
                raise ValidationError("Valid admin contract does not exist for this user")
            serializer.save(company=company, admin_contract=admin_contract)
        else:
            raise ValidationError("Only admins can create courses")

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
        temp_units = Temp_Unit.objects.filter(course=course)
        if self.request.user.is_trainer:
            for temp_unit in temp_units:
                # pend all units but the in delete state (to be deleted later in the approve)
                if not temp_unit.state == 'DE':
                    temp_unit.state = 'PE'
                    temp_unit.save()
                    temp_contents = Temp_Content.objects.filter(temp_unit=temp_unit)
                    # pend all the contetnts but the in delete state (to be deleted later in the approve)
                    for temp_content in temp_contents:
                        if not temp_content.state == 'DE':
                            temp_content.state = 'PE'
                            temp_content.save()
            return Response({'status': 'Published'}, status=status.HTTP_200_OK)
        else:
            raise ValidationError({'message': 'Cannot perform this action'})

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
        self.perform_create(self.get_serializer())
        return Response({'status': 'Approved'}, status=status.HTTP_200_OK)
    def perform_create(self, serializer):
        company_id = self.kwargs['company_id']
        course_id = self.kwargs['course_id']
        if self.request.user.is_admin:
            try:
                course = Course.objects.get(id=course_id, company_id=company_id)
            except Course.DoesNotExist:
                raise ValidationError({'message' : 'Course does not exist'})
            course.published = True
            course.save()
            # Check if all units and contents are in 'PE' state
            try:
                temp_units = Temp_Unit.objects.filter(course=course_id, state='PE')
            except Temp_Content.DoesNotExist:
                raise ValidationError({'message': 'No units in pending or delete state'})
            with transaction.atomic():
                for temp_unit in temp_units:
                    temp_contents = Temp_Content.objects.filter(temp_unit=temp_unit)
                    # get the original unit if there where a one 
                    if temp_unit.unit:
                        old_unit = Unit.objects.get(id=temp_unit.unit.id)
                    # If unit in state delete then delete it from the temp_unit
                    if temp_unit.state == 'DE':
                        temp_unit.delete()
                        if temp_unit.unit:
                            old_unit.delete()
                    elif temp_unit.state == 'PE':
                        if temp_unit.unit:
                            new_unit = Unit.objects.update(
                                id=temp_unit.unit.id,
                                course=course,
                                title=temp_unit.title,
                                order=temp_unit.order,
                                defaults={
                                    'title': old_unit.title,
                                    'order': old_unit.order,
                                }
                            )
                        else:
                            new_unit = Unit.objects.create(
                                course=course,
                                title=temp_unit.title,
                                order=temp_unit.order,
                            )
                        new_unit.save()
                        temp_unit.unit = new_unit
                        temp_unit.state = 'PU'
                        temp_unit.save()
                        for temp_content in temp_contents:
                            # get the old content if there were a one
                            if temp_content.content:
                                old_content = Content.objects.get(id=temp_content.content.id)
                            # If content in delete then delete it from the temp_content
                            if temp_content.state == 'DE':
                                temp_content.delete()
                                if temp_content.content:
                                    old_content.delete()
                            elif temp_content.state == 'PE':
                                if temp_content.content:
                                    new_content = Content.objects.update(
                                    id=temp_content.content.id,
                                    temp_unit=new_unit,
                                    title=temp_content.title,
                                    order=temp_content.order,
                                    is_video=temp_content.is_video,
                                    is_pdf=temp_content.is_pdf,
                                    is_test=temp_content.is_test,
                                    defaults={
                                        'temp_unit': temp_content.temp_unit,
                                        'title': temp_content.title,
                                        'order': temp_content.order,
                                        'is_video': temp_content.is_video,
                                        'is_pdf': temp_content.is_pdf,
                                        'is_test': temp_content.is_test,
                                    },
                                )
                                # Move Temp_Content to Content and mark them as 'PU'
                                new_content = Content.objects.create(
                                    unit=new_unit,
                                    title=temp_content.title,
                                    order=temp_content.order,
                                    is_video=temp_content.is_video,
                                    is_pdf=temp_content.is_pdf,
                                    is_test=temp_content.is_test
                                )
                                new_content.save()
                                temp_content.content = new_content
                                temp_content.state = 'PU'
                                temp_content.save()
                                # Move specific content type (Pdf, Video, Test) to access it from the content table
                                if temp_content.is_pdf:
                                    pdf = Pdf.objects.get(temp_content=temp_content)
                                    pdf.content = new_content
                                    pdf.temp_content = None
                                    pdf.save()
                                elif temp_content.is_video:
                                    video = Video.objects.get(temp_content=temp_content)
                                    video.content = new_content
                                    video.temp_content = None
                                    video.save()
                                elif temp_content.is_test:
                                    test = Test.objects.get(temp_content=temp_content)
                                    test.content = new_content
                                    test.temp_content = None
                                    test.save()
                # Change the course state to 'PU'
                course.state = 'PU'
                course.save()
        else:
            raise ValidationError({'message': 'Cannot perform this action'})

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
                admin_contract = Admin_Contract.objects.get(admin=user.admin, company__id=company_id, employed=True)
            except Admin_Contract.DoesNotExist:
                raise ValidationError("Admin contract does not exist for this user")
            try:
                course = Course.objects.filter(id=course_id, admin_contract=admin_contract, company=company_id)
            except Course.DoesNotExist:
                raise ValidationError('No such course for this admin in this company')
            return course
        # retrive the course if the trainer is whom created it
        elif user.is_trainer:
            try:
                trainer_contract = Trainer_Contract.objects.get(trainer=user.trainer, company__id=company_id, employed=True)
            except Trainer_Contract.DoesNotExist:
                raise ValidationError("Tranier contract does not exist for this user")            
            try:
                course = Course.objects.filter(id=course_id, company=company_id, trainer_contract_course__trainer_contract=trainer_contract)
            except Course.DoesNotExist:
                raise ValidationError('No such course for this trainer in this company')
            return course
        # retrive the course if the trainee has already enrolled in it 
        elif user.is_trainee:
            try:
                trainee_contract = Trainee_Contract.objects.get(trainee=user.trainee, company__id=company_id, employed=True)
            except Trainee_Contract.DoesNotExist:
                raise ValidationError("Trainee contract does not exist for this user")
            try:
                course = Course.objects.filter(id=course_id, enrollment__trainee_contract=trainee_contract, company=company_id)
            except Course.DoesNotExist:
                raise ValidationError('No such course for this trainee in this company')
            return course
        elif user.is_owner:
            try:
                course = Course.objects.filter(id=course_id, company__owner=user.owner)
            except Course.DoesNotExist:
                raise ValidationError('No such course for this owner in this company')
            return course
        else:
            return Response({'message': 'No Content'}, status=status.HTTP_204_NO_CONTENT)
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['view_type'] = 'detail'
        return context

# GET   : api/owner/company/:company-id/courses/course-id/part_not_part_users
# GET   : api/admin/company/:company-id/courses/course-id/part_not_part_users
class CompanyCourseRetrievePartandNotPartUsers(generics.ListAPIView):
    # set the serializer class
    serializer_class = User_Result_Serializer
    # set the permission class
    permission_classes = [IsAuthenticated, IsOwnerOrAdminForCourse]
    # set the lookup field to match the URL keyword argument
    lookup_url_kwarg = 'course_id'
    def get_queryset(self):
        company_id = self.kwargs['company_id']
        course_id = self.kwargs['course_id']
        result = []
        try:
            part_admin_contracts = Admin_Contract.objects.filter(course=course_id, company__id=company_id, employed=True)
            for admin_contract in part_admin_contracts:
                result.append({'user': admin_contract.admin.user, 'is_participant': True})
            part_trainer_contracts = Trainer_Contract.objects.filter(course=course_id, company__id=company_id, employed=True)
            for trainer_contract in part_trainer_contracts:
                result.append({'user': trainer_contract.trainer.user, 'is_participant': True})
            part_trainee_contracts = Trainee_Contract.objects.filter(course=course_id, company__id=company_id, employed=True)
            for trainee_contract in part_trainee_contracts:
                result.append({'user': trainee_contract.trainee.user, 'is_participant': True})
            admin_contracts = Admin_Contract.objects.filter(company__id=company_id, employed=True)
            for admin_contract in admin_contracts:
                if not any(res['user'] == admin_contract.admin.user for res in result):
                    result.append({'user': admin_contract.admin.user, 'is_participant': False})
            trainer_contracts = Trainer_Contract.objects.filter(company__id=company_id, employed=True)
            for trainer_contract in trainer_contracts:
                if not any(res['user'] == trainer_contract.trainer.user for res in result):
                    result.append({'user': trainer_contract.trainer.user, 'is_participant': False})
            trainee_contracts = Trainee_Contract.objects.filter(company__id=company_id, employed=True)
            for trainee_contract in trainee_contracts:
                if not any(res['user'] == trainee_contract.trainee.user for res in result):
                    result.append({'user': trainee_contract.trainee.user, 'is_participant': False})
        except (Admin_Contract.DoesNotExist, Trainer_Contract.DoesNotExist, Trainee_Contract.DoesNotExist):
            raise ValidationError({'message': 'Course or company not valid'})
        return result
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

# PUT   : api/owner/company/:company-id/courses/:course-id/set_trainer_leader
# PUT   : api/admin/company/:company-id/courses/:course-id/set_trainer_leader
class CompanyCourseSetTrainerLeader(generics.UpdateAPIView):
    # set the serializer class
    serializer_class = Trainer_Contract_Course_Leader_Serializer
    # set the permission class
    permission_classes = [IsAuthenticated, IsOwnerOrAdminForCourse]
    # set the lookup field to match the URL keyword argument
    lookup_url_kwarg = 'course_id'
    queryset = Trainer_Contract_Course.objects.all()
    def perform_update(self, serializer):
        company_id = self.kwargs['company_id']
        course_id = self.kwargs['course_id']
        trainer_contract = self.request.data.get('trainer_contract')
        result = []
        try:
            trainer_contract = Trainer_Contract.objects.get(id=trainer_contract, company__id=company_id, employed=True)
        except Trainer_Contract.DoesNotExist:
            raise ValidationError({'message': 'There is no such trainer contract'})
        try:
            trainer_contract_course = Trainer_Contract_Course.objects.get(
                trainer_contract=trainer_contract,
                trainer_contract__company=company_id,
                course=course_id
            )
        except Trainer_Contract_Course.DoesNotExist:
            raise ValidationError({'message': 'There is no trainer contract for this course'})
        # Set the trainer as a leader
        trainer_contract_course.is_leader = True
        trainer_contract_course.start_date = date.today()
        trainer_contract_course.save()
        # Retrieve all trainer contracts for the course
        all_trainer_contracts_course = Trainer_Contract_Course.objects.filter(course=course_id)
        [result.append(trainer_contract_course) for trainer_contract_course in all_trainer_contracts_course]
        return result

# GET   : api/admin/company/:company-id/pending_courses
class CompanyCourseListPending(generics.ListAPIView):
    # set the serializer class
    serializer_class = Course_Pending_Progress_Serializer
    # set the permission class
    permission_classes = [IsAuthenticated, IsCourseAdmin]
    # Document the view
    @swagger_auto_schema(
        operation_description='for presenting all the pended course details (all the main course data)',
        responses={200: course_list_response_body}
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    def get_queryset(self):    
        user = self.request.user
        company_id = self.kwargs['company_id']
        # retrive the course if the admin is whom created it
        if user.is_admin:
            try:
                admin_contract = Admin_Contract.objects.get(admin=user.admin, company__id=company_id, employed=True)
            except Admin_Contract.DoesNotExist:
                raise ValidationError("Admin contract does not exist for this user")
            try:
                courses = Course.objects.get(admin_contract=admin_contract, company=company_id)
            except Course.DoesNotExist:
                raise ValidationError({'message': 'pending course for this admin not found'})
            result_courses = []
            for course in courses:
                for unit in Temp_Unit.objects.filter(course=course):
                    if unit.state == 'PE':
                        result_courses.append(course)
                    for content in Temp_Content.objects.filter(temp_unit=unit):
                        if content.state == 'PE':
                            result_courses.append(course)
            try:
                courses = Course.objects.filter(id__in=[course.id for course in result_courses])
            except Course.DoesNotExist:
                raise ValidationError('No pending courses')
            return courses
    # when listing the courses set the view_type as list, otherwise set it as detail
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['view_type'] = 'list' if self.request.method == 'GET' else 'detail'
        return context

# GET   : api/admin/company/:company-id/pending_courses/course-id
class CompanyCourseRetrievePending(generics.RetrieveAPIView):
    # set the serializer class
    serializer_class = Course_Pending_Progress_Serializer
    # set the permission class
    permission_classes = [IsAuthenticated, IsCourseAdmin]
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
                admin_contract = Admin_Contract.objects.get(admin=user.admin, company__id=company_id, employed=True)
            except Admin_Contract.DoesNotExist:
                raise ValidationError("Admin contract does not exist for this user")
            try:
                course = Course.objects.get(id=course_id, admin_contract=admin_contract, company=company_id)
            except Course.DoesNotExist:
                raise ValidationError({'message': 'pending course for this admin not found'})
            units =  Temp_Unit.objects.filter(course=course, state='PE')
            contents = Temp_Content.objects.filter(temp_unit__in=units, state='PE')
            if units.exists() or contents.exists():
                try:
                    course = Course.objects.filter(id=course.id)
                except Course.DoesNotExist:
                    raise ValidationError('No such pending course')
                return course
            else:
                return Course.objects.none()
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['view_type'] = 'detail'
        return context

# GET   : api/trainer/company/:company-id/in_progress_courses
class CompanyCourseListInProgress(generics.ListAPIView):
    # set the serializer class
    serializer_class = Course_Pending_Progress_Serializer
    # set the permission class
    permission_classes = [IsAuthenticated, IsCourseTrainer]
    # Document the view
    @swagger_auto_schema(
        operation_description='for presenting all the pended course details (all the main course data)',
        responses={200: course_list_response_body}
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    def get_queryset(self):    
        user = self.request.user
        company_id = self.kwargs['company_id']
        # retrive the course if the admin is whom created it
        if user.is_trainer:
            try:
                trainer_contract = Trainer_Contract.objects.get(trainer=user.trainer, company__id=company_id, employed=True)
            except Trainer_Contract.DoesNotExist:
                raise ValidationError("Trainer contract does not exist for this user")
            try:
                courses = Course.objects.filter(trainers__id=trainer_contract.id, company=company_id)
            except Course.DoesNotExist:
                raise ValidationError({'message': 'did not find a course in progress for this trainer'})
            result_courses = []
            for course in courses:
                if not course.published:
                    result_courses.append(course)
                    continue
                for unit in Temp_Unit.objects.filter(course=course):
                    if unit.state == 'PR':
                        result_courses.append(course)
                    for content in Temp_Content.objects.filter(temp_unit=unit):
                        if content.state == 'PR':
                            result_courses.append(course)
            try:
                courses = Course.objects.filter(id__in=[course.id for course in result_courses])
            except Course.DoesNotExist:
                raise ValidationError('No courses in progress')
            return courses
    # when listing the courses set the view_type as list, otherwise set it as detail
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['view_type'] = 'list' if self.request.method == 'GET' else 'detail'
        return context

# GET   : api/trainer/company/:company-id/in_progress_courses/course-id
class CompanyCourseRetrieveInProgress(generics.RetrieveAPIView):
    # set the serializer class
    serializer_class = Course_Pending_Progress_Serializer
    # set the permission class
    permission_classes = [IsAuthenticated, IsCourseTrainer]
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
        is_in_progress = False
        # retrive the course if the admin is whom created it
        if user.is_trainer:
            try:
                trainer_contract = Trainer_Contract.objects.get(trainer=user.trainer, company__id=company_id, employed=True)
            except Trainer_Contract.DoesNotExist:
                raise ValidationError("Admin contract does not exist for this user")
            try:
                course = Course.objects.get(id=course_id, trainers=trainer_contract, company=company_id)
            except Course.DoesNotExist:
                raise ValidationError({'message': 'did not find a course in progress for this trainer'})
            for unit in Temp_Unit.objects.filter(course=course):
                if unit.state == 'PR':
                    is_in_progress = True
                for content in Temp_Content.objects.filter(temp_unit=unit):
                    if content.state == 'PR':
                        is_in_progress = True
            if not course.published:
                is_in_progress = True
            print(is_in_progress)
            if is_in_progress:
                print(course)
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
                admin_contract = Admin_Contract.objects.get(admin=user.admin, company__id=company_id, employed=True)
            except Admin_Contract.DoesNotExist:
                raise ValidationError("Admin contract does not exist for this user")
            try:
                course = Course.objects.filter(id=course_id, company=company_id, admin_contract=admin_contract)
            except Course.DoesNotExist:
                raise ValidationError('No such course for this admin in this company')
            return course
        # trainer can edit only his courses
        elif user.is_trainer:
            try:
                trainer_contract = Trainer_Contract.objects.get(trainer=user.trainer, company__id=company_id, employed=True)
            except Trainer_Contract.DoesNotExist:
                raise ValidationError("Tranier contract does not exist for this user")
            try:
                course = Course.objects.filter(id=course_id, company=company_id, trainer_contract=trainer_contract)
            except Course.DoesNotExist:
                raise ValidationError('No such course for this trainer in this company')
            return course
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
                admin_contract = Admin_Contract.objects.get(admin=user.admin, company__id=company_id, employed=True)
            except Admin_Contract.DoesNotExist:
                raise ValidationError("Admin contract does not exist for this user")
            try:
                course = Course.objects.filter(id=course_id, company=company_id, admin_contract=admin_contract)
            except Course.DoesNotExist:
                raise ValidationError('No such course for this admin')
            return course
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
                admin_contract = Admin_Contract.objects.get(admin=user.admin, company__id=company_id, employed=True)
            except Admin_Contract.DoesNotExist:
                raise ValidationError("Admin contract does not exist for this user")
            try:
                course = Course.objects.filter(id=course_id, company=company_id, admin_contract=admin_contract)
            except Course.DoesNotExist:
                raise ValidationError('No such course for this admin')
            return course
        # get the trainer courses
        elif user.is_trainer:
            try:
                trainer_contract = Trainer_Contract.objects.get(trainer=user.trainer, company__id=company_id, employed=True)
            except Trainer_Contract.DoesNotExist:
                raise ValidationError("Tranier contract does not exist for this user")
            try:
                course = Course.objects.filter(id=course_id, company=company_id, trainer_contract=trainer_contract)
            except Course.DoesNotExist:
                raise ValidationError('No such course for this trainer')
            return course
        # get the trainee courses
        elif user.is_trainee:
            try:
                trainee_contract = Trainee_Contract.objects.get(trainee=user.trainee, company__id=company_id, employed=True)
            except Trainee_Contract.DoesNotExist:
                raise ValidationError("Trainee contract does not exist for this user")
            try:
                course = Course.objects.filter(id=course_id, enrollment__Trainer_Contract=trainee_contract, company=company_id)
            except Course.DoesNotExist:
                raise ValidationError('No such course for this trainee')
            return course
        else:
            raise PermissionDenied("You do not have permission to view this course")
    # set the view_type to info (for sending all of the fields)
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['view_type'] = 'info'
        return context
    











class AdminCourseList(generics.ListAPIView):
      serializer_class = AdminCourseListSerializer
      permission_classes = [IsAuthenticated,IsAdminInCompanyOrOwner]
      def get_queryset(self): 
          return Course.objects.filter(company__id = self.kwargs["company_id"])
      

class TrainerPublishedCourseList(generics.ListAPIView):
      serializer_class = TrainerCourseListSerializer
      permission_classes = [IsAuthenticated]

      def get_queryset(self):
        user = self.request.user
        company_id = self.kwargs.get('company_id')
 
        trainer_contracts = Trainer_Contract.objects.filter(trainer__user=user, employed=True, company_id=company_id)

     
        courses = Course.objects.filter(
            company_id=company_id,
            trainers__in=trainer_contracts,
            published=True
        ).distinct()

        return courses
      

class TraineeCourseList(generics.ListAPIView):
      serializer_class = TraineeCourseListSerializer
      permission_classes = [IsAuthenticated]
     
     
      def get_queryset(self):
          user = self.request.user
          company_id = self.kwargs.get('company_id') 
          trainee_contracts = Trainee_Contract.objects.filter(trainee__user=user, employed=True, company_id=company_id)
          courses = Course.objects.filter(
              company__id=company_id,
              trainees__in=trainee_contracts,
              published = True
          ).distinct()
          return courses  