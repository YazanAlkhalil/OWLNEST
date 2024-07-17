from django.urls import path 
#views 
from system.views.CourseReportView import CourseReportView
from system.views.CommentView import ListCreateCommentView
from system.views.MarkContentAsCompleted import MarkContentView
from system.views.AddUserToCourse import AddUserToCourse
from system.views.TraineeCourseDashboard import TraineeCourseDashboard
from system.views.Reply import CreateReplyView
from system.views.TraineeMainDashboard import TraineeMainDashboardView
from system.views.ReactCommentView import ReactCommentView
from system.views.ReactReplyView import ReactReplyView
from system.views.AddToFavorite import AddToFavoriteView
urlpatterns = [
  #admin
    path('course/<id>/report',CourseReportView.as_view()),
    path('course/<id>/users',AddUserToCourse.as_view()),

  #trainee
    #comments
    path('course/<int:id>/comments',ListCreateCommentView.as_view()),
    path('course/<int:id>/comments/react',ReactCommentView.as_view()),
    #replies
    path('course/<id>/comments/reply',CreateReplyView.as_view()),
    path('course/<id>/comments/reply/react',ReactReplyView.as_view()),
   
    #mark as completed  
    path('mark-content-completed' , MarkContentView.as_view()),
    #course dashboard
    path('trainee/course/<id>/dashboard',TraineeCourseDashboard.as_view()),
    #main dashboard
    path('trainee/company/<id>/dashboard',TraineeMainDashboardView.as_view()),

    #favorites
    path('trainee/company/<id>/favorites', AddToFavoriteView.as_view()),
    
]

 