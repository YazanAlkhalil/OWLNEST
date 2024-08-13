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
from ..serializers.Course_Pending_InProgress import Course_Pending_Progress_Serializer
from ..serializers.User_Result import User_Result_Serializer
from ..serializers.Trainer_Contract_Course_Leader import Trainer_Contract_Course_Leader_Serializer
# permissions
from ..permissions.Owner import IsOwner, IsCompanyOwner, isCourseOwner
from ..permissions.Admin import IsAdmin, IsCompanyAdmin, IsCourseAdmin
from ..permissions.OwnerAdmin import IsOwnerOrAdmin, IsCompanyOwnerOrAdmin, IsCourseOwnerOrAdmin
from ..permissions.Trainer import IsTrainer, IsCompanyTrainer, IsCourseTrainer
from ..permissions.Trainee import IsTrainee, IsCompanyTrainee, IsCourseTrainee
# swagger
from drf_yasg.utils import swagger_auto_schema
from ..swagger.Course import (
    course_create_request_body, 
    course_list_response_body, 
    course_retrive_response_body, 
    course_retrive_info_response_body, 
    course_delete_response_body, 
    course_publish_approve_request_body
)

#############################################################
#                                                           #
#                                                           #
#               List Courses (All Published)                #
#                                                           #
#                                                           #
#############################################################

# GET : api/owner/company/:company-id/courses
class OwnerCourseList(generics.ListAPIView):
    serializer_class = Course_Serializer
    permission_classes = [IsAuthenticated, IsOwner, IsCompanyOwner]
    def get_queryset(self): 
        return Course.objects.filter(company__id=self.kwargs["company_id"])
    # when listing the courses set the view_type as list, otherwise set it as detail
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['view_type'] = 'list' if self.request.method == 'GET' else 'detail'
        context['user_type'] = 'owner'
        return context

# GET : api/admin/company/:company-id/courses
class AdminCourseList(generics.ListAPIView):
    serializer_class = Course_Serializer
    permission_classes = [IsAuthenticated, IsAdmin, IsCompanyAdmin]
    def get_queryset(self): 
        return Course.objects.filter(company__id=self.kwargs["company_id"])
    # when listing the courses set the view_type as list, otherwise set it as detail
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['view_type'] = 'list' if self.request.method == 'GET' else 'detail'
        context['user_type'] = 'admin'
        return context

# GET : api/trainer/company/:company-id/courses
class TrainerCourseList(generics.ListAPIView):
    serializer_class = Course_Serializer
    permission_classes = [IsAuthenticated, IsTrainer, IsCompanyTrainer]
    def get_queryset(self):
        user = self.request.user
        company_id = self.kwargs.get('company_id')
        trainer_contracts=Trainer_Contract.objects.filter(
            trainer__user=user, 
            employed=True, 
            company_id=company_id
        )
        courses = Course.objects.filter(
            company_id=company_id,
            trainers__in=trainer_contracts,
            published=True
        ).distinct()
        return courses
    # when listing the courses set the view_type as list, otherwise set it as detail
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['view_type'] = 'list' if self.request.method == 'GET' else 'detail'
        context['user_type'] = 'trainer'
        return context

# GET : api/trainee/company/:company-id/courses
class TraineeCourseList(generics.ListAPIView):
    serializer_class = Course_Serializer
    permission_classes = [IsAuthenticated, IsTrainee, IsCompanyTrainee]
    def get_queryset(self):
        user = self.request.user
        company_id = self.kwargs.get('company_id') 
        trainee_contracts = Trainee_Contract.objects.filter(
            trainee__user=user, 
            employed=True, 
            company_id=company_id
        )
        courses = Course.objects.filter(
            company__id=company_id,
            trainees__in=trainee_contracts,
            published = True
        ).annotate(
            progress=F('enrollment__progress'),
            is_favorite=Exists(Favorite.objects.filter(enrollment__course=OuterRef('pk'), trainee_contract__in=trainee_contracts))
        )
        return courses  
    # when listing the courses set the view_type as list, otherwise set it as detail
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['view_type'] = 'list' if self.request.method == 'GET' else 'detail'
        context['user_type'] = 'trainee'
        return context

#############################################################
#                                                           #
#                                                           #
#               Retrieve Course (Published)                 #
#                                                           #
#                                                           #
#############################################################

# GET   : api/owner/company/:company-id/courses/course-id
class OwnerCourseRetrieve(generics.RetrieveAPIView):
    # set the serializer class
    serializer_class = Course_Serializer
    # set the permission class
    permission_classes = [IsAuthenticated, IsOwner, IsCompanyOwner]
    # set the lookup field to match the URL keyword argument
    lookup_url_kwarg = 'course_id'
    lookup_field = 'id'
    # Document the view
    @swagger_auto_schema(
        operation_description='for presenting a specific course details (all the main course data) \nNote: that this is not for the info page which present the whole information about the course and the additional resources',
        responses={200: course_retrive_response_body}
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    def get_queryset(self):
        return Course.objects.filter(company=self.kwargs['company_id'])
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['view_type'] = 'detail'
        context['user_type'] = 'owner'
        return context

# GET   : api/admin/company/:company-id/courses/course-id
class AdminCourseRetrieve(generics.RetrieveAPIView):
    # set the serializer class
    serializer_class = Course_Serializer
    # set the permission class
    permission_classes = [IsAuthenticated, IsAdmin, IsCompanyAdmin]
    # set the lookup field to match the URL keyword argument
    lookup_url_kwarg = 'course_id'
    lookup_field = 'id'
    # Document the view
    @swagger_auto_schema(
        operation_description='for presenting a specific course details (all the main course data) \nNote: that this is not for the info page which present the whole information about the course and the additional resources',
        responses={200: course_retrive_response_body}
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    def get_queryset(self):
        return Course.objects.filter(company=self.kwargs['company_id'])
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['view_type'] = 'detail'
        context['user_type'] = 'admin'
        return context

# GET   : api/trainer/company/:company-id/courses/course-id
class TrainerCourseRetrieve(generics.RetrieveAPIView):
    # set the serializer class
    serializer_class = Course_Serializer
    # set the permission class
    permission_classes = [IsAuthenticated, IsTrainer, IsCompanyTrainer, IsCourseTrainer]
    # set the lookup field to match the URL keyword argument
    lookup_url_kwarg = 'course_id'
    lookup_field = 'id'
    # Document the view
    @swagger_auto_schema(
        operation_description='for presenting a specific course details (all the main course data) \nNote: that this is not for the info page which present the whole information about the course and the additional resources',
        responses={200: course_retrive_response_body}
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    def get_queryset(self):
        return Course.objects.filter(company=self.kwargs['company_id'])
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['view_type'] = 'detail'
        context['user_type'] = 'trainer'
        return context

# GET   : api/trainee/company/:company-id/courses/course-id
class TraineeCourseRetrieve(generics.RetrieveAPIView):
    # set the serializer class
    serializer_class = Course_Serializer
    # set the permission class
    permission_classes = [IsAuthenticated, IsTrainee, IsCompanyTrainee, IsCourseTrainee]
    # set the lookup field to match the URL keyword argument
    lookup_url_kwarg = 'course_id'
    lookup_field = 'id'
    # Document the view
    @swagger_auto_schema(
        operation_description='for presenting a specific course details (all the main course data) \nNote: that this is not for the info page which present the whole information about the course and the additional resources',
        responses={200: course_retrive_response_body}
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    def get_queryset(self):
        return Course.objects.filter(company=self.kwargs['company_id'])
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['view_type'] = 'detail'
        context['user_type'] = 'trainee'
        return context


#############################################################
#                                                           #
#                                                           #
#                  List Courses (InProgress)                #
#                 Retrieve Course (InProgress)              #
#                                                           #
#                                                           #
#############################################################

# GET   : api/trainer/company/:company-id/in_progress_courses
class CompanyCourseListInProgress(generics.ListAPIView):
    # set the serializer class
    serializer_class = Course_Pending_Progress_Serializer
    # set the permission class
    permission_classes = [IsAuthenticated, IsTrainer, IsCompanyTrainer, IsCourseTrainer]
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
        try:
            trainer_contract = Trainer_Contract.objects.get(trainer=user.trainer, company__id=company_id, employed=True)
        except Trainer_Contract.DoesNotExist:
            raise ValidationError({'message': "Trainer contract does not exist for this user"})
        try:
            courses = Course.objects.filter(trainers=trainer_contract, company=company_id)
        except Course.DoesNotExist:
            raise ValidationError({'message': 'did not find a course in progress for this trainer'})
        result_courses = []
        for course in courses:
            if not course.published:
                result_courses.append(course)
                continue
            for unit in Temp_Unit.objects.filter(course=course):
                if unit.state == 'PR' or unit.state == 'DE':
                    result_courses.append(course)
                for content in Temp_Content.objects.filter(temp_unit=unit):
                    if content.state == 'PR' or content.state == 'DE':
                        result_courses.append(course)
        try:
            courses = Course.objects.filter(id__in=[course.id for course in result_courses])
        except Course.DoesNotExist:
            raise ValidationError({'message': 'No courses in progress'})
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
    permission_classes = [IsAuthenticated, IsTrainer, IsCompanyTrainer, IsCourseTrainer]
    # set the lookup field to match the URL keyword argument
    lookup_url_kwarg = 'course_id'
    lookup_field = 'id'
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
        try:
            trainer_contract = Trainer_Contract.objects.get(trainer=user.trainer, trainer_contract_course__course=course_id, company__id=company_id, employed=True)
        except Trainer_Contract.DoesNotExist:
            raise ValidationError({'message': "Trainer contract does not exist for this user"})
        try:
            course = Course.objects.get(id=course_id, trainers=trainer_contract, company=company_id)
        except Course.DoesNotExist:
            raise ValidationError({'message': 'did not find a course in progress for this trainer'})
        for unit in Temp_Unit.objects.filter(course=course):
            if unit.state == 'PR' or unit.state == 'DE':
                is_in_progress = True
            for content in Temp_Content.objects.filter(temp_unit=unit):
                if content.state == 'PR' or content.state == 'DE':
                    is_in_progress = True
        if not course.published:
            is_in_progress = True
        if is_in_progress:
            try:
                course = Course.objects.filter(id=course.id)
            except Course.DoesNotExist:
                raise ValidationError({'message': 'No such course in progress'})
            return course
        else:
            raise ValidationError({'message': 'No Contect'})
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['view_type'] = 'detail'
        return context

#############################################################
#                                                           #
#                                                           #
#                   List Courses (Pending)                  #
#                  Retrieve Course (Pending)                #
#                                                           #
#                                                           #
#############################################################

# GET   : api/admin/company/:company-id/pending_courses
class CompanyCourseListPending(generics.ListAPIView):
    # set the serializer class
    serializer_class = Course_Pending_Progress_Serializer
    # set the permission class
    permission_classes = [IsAuthenticated, IsAdmin, IsCompanyAdmin, IsCourseAdmin]
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
        try:
            admin_contract = Admin_Contract.objects.get(admin=user.admin, company__id=company_id, employed=True)
        except Admin_Contract.DoesNotExist:
            raise ValidationError({'message': "Admin contract does not exist for this user"})
        try:
            courses = Course.objects.filter(admin_contract=admin_contract, company=company_id)
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
            raise ValidationError({'message': 'No pending courses'})
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
    permission_classes = [IsAuthenticated, IsAdmin, IsCompanyAdmin, IsCourseAdmin]
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
        try:
            admin_contract = Admin_Contract.objects.get(admin=user.admin, company__id=company_id, employed=True)
        except Admin_Contract.DoesNotExist:
            raise ValidationError({'message': "Admin contract does not exist for this user"})
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
                raise ValidationError({'message': 'No such pending course'})
            return course
        else:
            return Course.objects.none()
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['view_type'] = 'detail'
        return context

#############################################################
#                                                           #
#                                                           #
#                Create Course (Only Admin)                 #
#                                                           #
#                                                           #
#############################################################

# POST: api/admin/company/:company-id/courses
class CompanyCourseCreate(generics.CreateAPIView):
    # set the serializer class
    serializer_class = Course_Serializer
    # set the permission class
    permission_classes = [IsAuthenticated, IsAdmin, IsCompanyAdmin]
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
            raise ValidationError({'message': 'Company does not exist'})
        try:
            admin_contract = Admin_Contract.objects.get(admin=user.admin, company__id=company_id, employed=True)
        except Admin_Contract.DoesNotExist:
            raise ValidationError({'message': "Valid admin contract does not exist for this user"})
        serializer.save(company=company, admin_contract=admin_contract)

#############################################################
#                                                           #
#                                                           #
#                 Publish Course (Only Trainer)             #
#                                                           #
#                                                           #
#############################################################

# POST: api/trainer/company/:company_id/courses/:course_id/publish
class CompanyCoursePublish(generics.UpdateAPIView):
    # set the serializer class
    serializer_class = Course_Serializer
    # set the permission class
    permission_classes = [IsAuthenticated, IsTrainer, IsCompanyTrainer, IsCourseTrainer]
    @swagger_auto_schema(
        operation_description='Publish a specific course with all its units and contents',
        request_body=course_publish_approve_request_body,
        responses={200: 'Published'}
    )
    def post(self, request, *args, **kwargs):
        company_id = self.kwargs['company_id']
        course_id = self.kwargs['course_id']
        try:
            course = Course.objects.get(id=course_id, company_id=company_id)
        except Course.DoesNotExist:
            raise ValidationError({'message': 'Did not found the course'})
        try:
            temp_units = Temp_Unit.objects.filter(course=course)
        except Temp_Unit.DoesNotExist:
            raise ValidationError({'message': 'Did not found the in progress units for this course'})
        for temp_unit in temp_units:
            # pend all units but the in delete state (to be deleted later in the approve)
            if temp_unit.state == 'PR':
                temp_unit.state = 'PE'
                temp_unit.save()
                temp_contents = Temp_Content.objects.filter(temp_unit=temp_unit)
                # pend all the contetnts but the in delete state (to be deleted later in the approve)
                for temp_content in temp_contents:
                    if temp_content.state == 'PR':
                        temp_content.state = 'PE'
                        temp_content.save()
        return Response({'status': 'Published'}, status=status.HTTP_200_OK)

#############################################################
#                                                           #
#                                                           #
#                 Approve Course (Only Admin)               #
#                                                           #
#                                                           #
#############################################################

# POST: api/admin/company/:company_id/courses/:course_id/approve
class CompanyCourseApprove(generics.CreateAPIView):
    # set the serializer class
    serializer_class = Course_Serializer
    # set the permission class
    permission_classes = [IsAuthenticated, IsAdmin, IsCompanyAdmin, IsCourseAdmin]
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
        try:
            course = Course.objects.get(id=course_id, company_id=company_id)
        except Course.DoesNotExist:
            raise ValidationError({'message' : 'Course does not exist'})
        # Check if all units and contents are in 'PE' state
        try:
            temp_units = Temp_Unit.objects.filter(course=course)
        except Temp_Unit.DoesNotExist:
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
                        temp_unit.unit.course=course
                        temp_unit.unit.title=temp_unit.title
                        temp_unit.unit.order=temp_unit.order
                    else:
                        new_unit = Unit.objects.create(
                            course=course,
                            title=temp_unit.title,
                            published=True,
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
                                temp_content.content.title = temp_content.title
                                temp_content.content.order = temp_content.order
                                temp_content.content.is_video = temp_content.is_video
                                temp_content.content.is_pdf = temp_content.is_pdf
                                temp_content.content.is_test = temp_content.is_test
                            else:
                                new_content = Content.objects.create(
                                    unit=temp_unit.unit,
                                    title=temp_content.title,
                                    order=temp_content.order,
                                    published=True,
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
                                try:
                                    pdf = Pdf.objects.get(temp_content=temp_content)
                                except Pdf.DoesNotExist:
                                    try:
                                        pdf = Pdf.objects.get(content=temp_content.content)
                                    except Pdf.DoesNotExist:
                                        raise ValidationError({'message': 'pdf does not exists'})
                                pdf.content = temp_content.content
                                pdf.temp_content = None
                                pdf.save()
                            elif temp_content.is_video:
                                try:
                                    video = Video.objects.get(temp_content=temp_content)
                                except Video.DoesNotExist:
                                    try:
                                        video = Video.objects.get(content=temp_content.content)
                                    except Video.DoesNotExist:
                                        raise ValidationError({'message': 'video does not exists'})
                                video.content = temp_content.content
                                video.temp_content = None
                                video.save()
                            elif temp_content.is_test:
                                try:
                                    test = Test.objects.get(temp_content=temp_content)
                                except Test.DoesNotExist:
                                    try:
                                        test = Test.objects.get(content=temp_content.content)
                                    except Test.DoesNotExist:
                                        raise ValidationError({'message': 'test does not exists'})
                                test.content = temp_content.content
                                test.temp_content = None
                                test.save()
            # Change the course state to 'PU'
            course.published = True
            course.save()

#############################################################
#                                                           #
#                                                           #
#              Disapprove Course (Only Admin)               #
#                                                           #
#                                                           #
#############################################################

# POST: api/admin/company/:company_id/courses/:course_id/disapprove
class CompanyCourseDisapprove(generics.CreateAPIView):
    # set the serializer class
    serializer_class = Course_Serializer
    # set the permission class
    permission_classes = [IsAuthenticated, IsAdmin, IsCompanyAdmin, IsCourseAdmin]
    @swagger_auto_schema(
        operation_description='Disapprove a specific course with all its units and contents',
        request_body=course_publish_approve_request_body,
        responses={200: 'Disapproved'}
    )
    def post(self, request, *args, **kwargs):
        self.perform_create(self.get_serializer())
        return Response({'status': 'Disapproved'}, status=status.HTTP_200_OK)
    def perform_create(self, serializer):
        company_id = self.kwargs['company_id']
        course_id = self.kwargs['course_id']
        try:
            course = Course.objects.get(id=course_id, company_id=company_id)
        except Course.DoesNotExist:
            raise ValidationError({'message' : 'Course does not exist'})
        # Check if all units and contents are in 'PE' state
        try:
            temp_units = Temp_Unit.objects.filter(course=course)
        except Temp_Unit.DoesNotExist:
            raise ValidationError({'message': 'No units in pending or delete state'})
        with transaction.atomic():
            for temp_unit in temp_units:
                temp_contents = Temp_Content.objects.filter(temp_unit=temp_unit)
                # get the original unit if there where a one 
                if temp_unit.unit:
                    old_unit = Unit.objects.get(id=temp_unit.unit.id)
                # If unit in state delete then delete it from the temp_unit
                if temp_unit.state == 'DE':
                    temp_unit.state = 'PU'
                elif temp_unit.state == 'PE':
                    temp_unit.delete()
                for temp_content in temp_contents:
                    # get the old content if there were a one
                    if temp_content.content:
                        old_content = Content.objects.get(id=temp_content.content.id)
                    # If content in delete then delete it from the temp_content
                    if temp_content.state == 'DE':
                        temp_content.state = 'PU'
                    elif temp_content.state == 'PE':    
                        temp_content.delete()
                    # Move specific content type (Pdf, Video, Test) to access it from the content table
                    # if temp_content.is_pdf:
                    #     if temp_content.content:    
                    #         try:
                    #             pdf = Pdf.objects.get(temp_content=temp_content)
                    #         except Pdf.DoesNotExist:
                    #             raise ValidationError({'message': 'pdf does not exists'})
                    #         pdf.content = temp_content.content
                    #         pdf.temp_content = None
                    #         pdf.save()
                    #     else:
                    #         pdf.delete()
                    # elif temp_content.is_video:
                    #     if temp_content.content:
                    #         try:
                    #             video = Video.objects.get(temp_content=temp_content)
                    #         except Video.DoesNotExist:    
                    #             raise ValidationError({'message': 'video does not exists'})
                    #         video.content = temp_content.content
                    #         video.temp_content = None
                    #         video.save()
                    #     else:
                    #         video.delete()
                    # elif temp_content.is_test:
                    #     if temp_content.content:
                    #         try:
                    #             test = Test.objects.get(temp_content=temp_content)
                    #         except Test.DoesNotExist:
                    #             raise ValidationError({'message': 'test does not exists'})
                    #         test.content = temp_content.content
                    #         test.temp_content = None
                    #         test.save()
                    #     else:
                    #         test.delete()

#################################################################################
#                                                                               #
#                                                                               #
#    Retrive All Company Users For Course (Parts And Not Parts In The Course)   #
#                                                                               #
#                                                                               #
#################################################################################

# GET   : api/owner/company/:company-id/courses/course-id/part_not_part_users
# GET   : api/admin/company/:company-id/courses/course-id/part_not_part_users
class CompanyCourseRetrievePartandNotPartUsers(generics.ListAPIView):
    # set the serializer class
    serializer_class = User_Result_Serializer
    # set the permission class
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin, IsCompanyOwnerOrAdmin, IsCourseOwnerOrAdmin]
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

#################################################################################
#                                                                               #
#                                                                               #
#    Retrive All Company Users For Course (Parts And Not Parts In The Course)   #
#                                                                               #
#                                                                               #
#################################################################################

# PUT   : api/owner/company/:company-id/courses/:course-id/set_trainer_leader
# PUT   : api/admin/company/:company-id/courses/:course-id/set_trainer_leader
class CompanyCourseSetTrainerLeader(generics.UpdateAPIView):
    # set the serializer class
    serializer_class = Trainer_Contract_Course_Leader_Serializer
    # set the permission class
    permission_classes = [IsAuthenticated, isCourseOwner, IsCompanyOwnerOrAdmin, IsCourseOwnerOrAdmin]
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

##########################
#                        #
#                        #
#      Update Course     #
#                        #
#                        #
##########################

# PUT   : api/admin/company/:company-id/courses/:course-id
class CompanyCourseUpdateAdmin(generics.UpdateAPIView):
    # set the serializer class
    serializer_class = Course_Serializer
    # set the permission class
    permission_classes = [IsAuthenticated, IsAdmin, IsCompanyAdmin, IsCourseAdmin]
    # set the lookup field to match the URL keyword argument
    lookup_url_kwarg = 'course_id'
    # Document the view
    @swagger_auto_schema(
        operation_description='for presenting a specific course details (all the main course data) \nNote: that this is not for the info page which present the whole information about the course and the additional resources',
        request_body=Course_Serializer,
        responses={200: course_retrive_response_body}
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)
    def get_queryset(self):
        user = self.request.user
        company_id = self.kwargs['company_id']
        course_id = self.kwargs['course_id']
        try:
            admin_contract = Admin_Contract.objects.get(admin=user.admin, company__id=company_id, employed=True)
        except Admin_Contract.DoesNotExist:
            raise ValidationError({'message': "Admin contract does not exist for this user"})
        try:
            course = Course.objects.filter(id=course_id, company=company_id, admin_contract=admin_contract)
        except Course.DoesNotExist:
            raise ValidationError({'message': 'No such course for this admin in this company'})
        return course
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['view_type'] = 'detail'
        context['user_type'] = 'admin'
        return context

# PUT   : api/trainer/company/:company-id/courses/:course-id
class CompanyCourseUpdateTrainer(generics.UpdateAPIView):
    # set the serializer class
    serializer_class = Course_Serializer
    # set the permission class
    permission_classes = [IsAuthenticated, IsTrainer, IsCompanyTrainer, IsCourseTrainer]
    # set the lookup field to match the URL keyword argument
    lookup_url_kwarg = 'course_id'
    # Document the view
    @swagger_auto_schema(
        operation_description='for presenting a specific course details (all the main course data) \nNote: that this is not for the info page which present the whole information about the course and the additional resources',
        request_body=Course_Serializer,
        responses={200: course_retrive_response_body}
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)
    def get_queryset(self):
        user = self.request.user
        company_id = self.kwargs['company_id']
        course_id = self.kwargs['course_id']
        try:
            trainer_contract = Trainer_Contract.objects.get(trainer=user.trainer, company__id=company_id, employed=True)
        except Trainer_Contract.DoesNotExist:
            raise ValidationError({'message': "Tranier contract does not exist for this user"})
        try:
            course = Course.objects.filter(id=course_id, company=company_id, trainer_contract=trainer_contract)
        except Course.DoesNotExist:
            raise ValidationError({'message': 'No such course for this trainer in this company'})
        return course
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['view_type'] = 'detail'
        context['user_type'] = 'trainer'
        return context

##########################
#                        #
#                        #
#      Delete Course     #
#                        #
#                        #
##########################

# DELETE: api/admin/company/:company-id/courses/course-id
class CompanyCourseDelete(generics.DestroyAPIView):
    # set the serializer class
    serializer_class = Course_Serializer
    # set the permission class
    permission_classes = [IsAuthenticated, IsAdmin, IsCompanyAdmin, IsCourseAdmin]
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
        try:
            admin_contract = Admin_Contract.objects.get(admin=user.admin, company__id=company_id, employed=True)
        except Admin_Contract.DoesNotExist:
            raise ValidationError({'message': "Admin contract does not exist for this user"})
        try:
            course = Course.objects.filter(id=course_id, company=company_id, admin_contract=admin_contract)
        except Course.DoesNotExist:
            raise ValidationError({'message': 'No such course for this admin'})
        return course
    def perform_destroy(self, instance):
        user = self.request.user
        if user.is_trainer or user.is_trainee:
            raise PermissionDenied({'message': "You do not have permission to delete courses"})
        instance.delete()
        return Response({'message':'Course Deleted'}, status=204)

#####################################
#                                   #
#                                   #
#      Retrive Course Full Info     #
#                                   #
#                                   #
#####################################

# GET   : api/owner/company/:company-id/courses/course-id/info
class OwnerCourseRetriveInfo(generics.RetrieveAPIView):
    # set the serializer class
    serializer_class = Course_Serializer
    # set the permission class
    permission_classes = [IsAuthenticated, IsOwner, IsCompanyOwner, isCourseOwner]
    # set the lookup field to match the URL keyword argument
    lookup_url_kwarg = 'course_id'
    lookup_field = 'id'
    # Document the view
    @swagger_auto_schema(
        operation_description="Retrieve a specific course whole information from a specific company for the extra page with the additional info and stuff",
        responses={200: course_retrive_info_response_body}
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    def get_queryset(self):    
        company_id = self.kwargs['company_id']
        try:
            return Course.objects.filter(company=company_id)
        except Course.DoesNotExist:
            raise ValidationError({'message': 'No such course for this owner'})
    # set the view_type to info (for sending all of the fields)
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['view_type'] = 'info'
        context['user_type'] = 'owner'
        return context

# GET   : api/admin/company/:company-id/courses/course-id/info
class AdminCourseRetriveInfo(generics.RetrieveAPIView):
    # set the serializer class
    serializer_class = Course_Serializer
    # set the permission class
    permission_classes = [IsAuthenticated, IsAdmin, IsCompanyAdmin, IsCourseAdmin]
    # set the lookup field to match the URL keyword argument
    lookup_url_kwarg = 'course_id'
    lookup_field = 'id'
    # Document the view
    @swagger_auto_schema(
        operation_description="Retrieve a specific course whole information from a specific company for the extra page with the additional info and stuff",
        responses={200: course_retrive_info_response_body}
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    def get_queryset(self):    
        company_id = self.kwargs['company_id']
        try:
            return Course.objects.filter(company=company_id)
        except Course.DoesNotExist:
            raise ValidationError({'message': 'No such course for this admin'})
    # set the view_type to info (for sending all of the fields)
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['view_type'] = 'info'
        context['user_type'] = 'admin'
        return context

# GET   : api/trainer/company/:company-id/courses/course-id/info
class TrainerCourseRetriveInfo(generics.RetrieveAPIView):
    # set the serializer class
    serializer_class = Course_Serializer
    # set the permission class
    permission_classes = [IsAuthenticated, IsTrainer, IsCompanyTrainer, IsCourseTrainer]
    # set the lookup field to match the URL keyword argument
    lookup_url_kwarg = 'course_id'
    lookup_field = 'id'
    # Document the view
    @swagger_auto_schema(
        operation_description="Retrieve a specific course whole information from a specific company for the extra page with the additional info and stuff",
        responses={200: course_retrive_info_response_body}
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    def get_queryset(self):
        company_id = self.kwargs['company_id']
        try:
            return Course.objects.filter(company=company_id)
        except Course.DoesNotExist:
            raise ValidationError({'message': 'No such course for this trainer'})
    # set the view_type to info (for sending all of the fields)
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['view_type'] = 'info'
        context['user_type'] = 'trainer'
        return context

# GET   : api/trainee/company/:company-id/courses/course-id/info
class TraineeCourseRetriveInfo(generics.RetrieveAPIView):
    # set the serializer class
    serializer_class = Course_Serializer
    # set the permission class
    permission_classes = [IsAuthenticated, IsTrainee, IsCompanyTrainee, IsCourseTrainee]
    # set the lookup field to match the URL keyword argument
    lookup_url_kwarg = 'course_id'
    lookup_field = 'id'
    # Document the view
    @swagger_auto_schema(
        operation_description="Retrieve a specific course whole information from a specific company for the extra page with the additional info and stuff",
        responses={200: course_retrive_info_response_body}
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    def get_queryset(self):    
        company_id = self.kwargs['company_id']
        try:
            return Course.objects.filter(company=company_id)
        except Course.DoesNotExist:
            raise ValidationError({'message': 'No such course for this trainee'})
    # set the view_type to info (for sending all of the fields)
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['view_type'] = 'info'
        context['user_type'] = 'trainee'
        return context