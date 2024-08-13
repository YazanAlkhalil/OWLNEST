from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from ..views.Course import (
    OwnerCourseList,
    AdminCourseList,
    TrainerCourseList,
    TraineeCourseList,
    OwnerCourseRetrieve,
    AdminCourseRetrieve,
    TrainerCourseRetrieve,
    TraineeCourseRetrieve,
    CompanyCourseCreate, 
    CompanyCourseListInProgress, 
    CompanyCourseRetrieveInProgress, 
    CompanyCoursePublish, 
    CompanyCourseListPending, 
    CompanyCourseRetrievePending,
    CompanyCourseApprove,
    CompanyCourseDisapprove, 
    CompanyCourseRetrievePartandNotPartUsers, 
    CompanyCourseSetTrainerLeader, 
    CompanyCourseUpdateAdmin, 
    CompanyCourseUpdateTrainer,
    CompanyCourseDelete, 
    OwnerCourseRetriveInfo,
    AdminCourseRetriveInfo,
    TrainerCourseRetriveInfo,
    TraineeCourseRetriveInfo
)

urlpatterns = [
    ##############
    #    List    #
    ##############
    path(
        'owner/company/<int:company_id>/courses', 
        OwnerCourseList.as_view(), 
        name='company-course-owner-list'
    ),
    path(
        'admin/company/<int:company_id>/courses', 
        AdminCourseList.as_view(), 
        name='company-course-admin-list'
    ),
    path(
        'trainer/company/<int:company_id>/courses', 
        TrainerCourseList.as_view(), 
        name='company-course-trainer-list'
    ),
    path(
        'trainee/company/<int:company_id>/courses', 
        TraineeCourseList.as_view(), 
        name='company-course-trainee-list'
    ),
    ##############
    #  Retrieve  #
    ##############
    path(
        'owner/company/<int:company_id>/courses/<int:course_id>', 
        OwnerCourseRetrieve.as_view(), 
        name='company-course-owner-retrive'
    ),
    path(
        'admin/company/<int:company_id>/courses/<int:course_id>', 
        AdminCourseRetrieve.as_view(), 
        name='company-course-admin-retrive'
    ),
    path(
        'trainer/company/<int:company_id>/courses/<int:course_id>', 
        TrainerCourseRetrieve.as_view(), 
        name='company-course-trainer-retrive'
    ),
    path(
        'trainee/company/<int:company_id>/courses/<int:course_id>', 
        TraineeCourseRetrieve.as_view(), 
        name='company-course-trainee-retrive'
    ),
    #######################
    #   List InProgress   #
    #######################
    path(
        'trainer/company/<int:company_id>/progress_courses', 
        CompanyCourseListInProgress.as_view(), 
        name='company-progress-course-trainer-list'
    ),
    ##########################
    #   Retrieve InProgress  #
    ##########################
    path(
        'trainer/company/<int:company_id>/progress_courses/<int:course_id>', 
        CompanyCourseRetrieveInProgress.as_view(), 
        name='company-progress-course-trainer-retrive'
    ),
    ####################
    #   List Pending   #
    ####################
    path(
        'admin/company/<int:company_id>/pending_courses', 
        CompanyCourseListPending.as_view(), 
        name='company-pending-course-admin-list'
    ),
    ########################
    #   Retrieve Pending   #
    ########################
    path(
        'admin/company/<int:company_id>/pending_courses/<int:course_id>', 
        CompanyCourseRetrievePending.as_view(), 
        name='company-pending-course-admin-retrive'
    ),
    ##############
    #   Create   #
    ##############
    path(
        'admin/company/<int:company_id>/courses/create', 
        CompanyCourseCreate.as_view(), 
        name='company-course-admin-create'
    ),
    ###############
    #   Publish   #
    ###############
    path(
        'trainer/company/<int:company_id>/courses/<int:course_id>/publish', 
        CompanyCoursePublish.as_view(), 
        name='company-course-trainer-publish'
    ),
    ###############
    #   Approve   #
    ###############
    path(
        'admin/company/<int:company_id>/courses/<int:course_id>/approve', 
        CompanyCourseApprove.as_view(), 
        name='company-course-admin-approve'
    ),
    ##################
    #   Disapprove   #
    ##################
    path(
        'admin/company/<int:company_id>/courses/<int:course_id>/disapprove', 
        CompanyCourseDisapprove.as_view(), 
        name='company-course-admin-disapprove'
    ),
    ########################################################
    #   Part And Not Part Users From Company In A Course   #
    ########################################################
    path(
        'owner/company/<int:company_id>/courses/<int:course_id>/part_not_part_users', 
        CompanyCourseRetrievePartandNotPartUsers.as_view(), 
        name='company-course-owner-retrive-part-not-part-users'
    ),
    path(
        'admin/company/<int:company_id>/courses/<int:course_id>/part_not_part_users', 
        CompanyCourseRetrievePartandNotPartUsers.as_view(), 
        name='company-course-admin-retrive-part-not-part-users'
    ),
    ###############################
    #   Set Leader For A Course   #
    ###############################
    path(
        'owner/company/<int:company_id>/courses/<int:course_id>/set_trainer_leader',
        CompanyCourseSetTrainerLeader.as_view(),
        name='company-course-owner-set-leader'
    ),
    path(
        'admin/company/<int:company_id>/courses/<int:course_id>/set_trainer_leader',
        CompanyCourseSetTrainerLeader.as_view(),
        name='company-course-admin-set-leader'
    ),
    ##############
    #   Update   #
    ##############
    path(
        'admin/company/<int:company_id>/courses/<int:course_id>/update', 
        CompanyCourseUpdateAdmin.as_view(), 
        name='company-course-admin-update'
    ),
    path(
        'trainer/company/<int:company_id>/courses/<int:course_id>/update', 
        CompanyCourseUpdateTrainer.as_view(), 
        name='company-course-trainer-update'
    ),
    ##############
    #   Delete   #
    ##############
    path(
        'admin/company/<int:company_id>/courses/<int:course_id>/delete',
        CompanyCourseDelete.as_view(),
        name='company-course-admin-delete'
    ),
    ################################
    #   Retrive Course Full Info   #
    ################################
    path(
        'owner/company/<int:company_id>/courses/<int:course_id>/info',
        OwnerCourseRetriveInfo.as_view(),
        name='company-course-admin-info'
    ),
    path(
        'admin/company/<int:company_id>/courses/<int:course_id>/info',
        AdminCourseRetriveInfo.as_view(),
        name='company-course-admin-info'
    ),
    path(
        'trainer/company/<int:company_id>/courses/<int:course_id>/info',
        TrainerCourseRetriveInfo.as_view(),
        name='company-course-trainer-info'
    ),  
    path(
        'trainee/company/<int:company_id>/courses/<int:course_id>/info',
        TraineeCourseRetriveInfo.as_view(),
        name='company-course-trainee-info'
    ),
]
# adding the urls for the static files (course image)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)