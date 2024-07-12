from django.urls import path 
#views 
from system.views.CourseReportView import CourseReportView
from system.views.Comment import ListCreateCommentView
from system.views.MarkContentAsCompleted import MarkContentView
from system.views.AddUserToCourse import AddUserToCourse
from system.views.TraineeCourseDashboard import TraineeCourseDashboard
from system.views.Reply import CreateReplyView
urlpatterns = [
  #admin
  path('course/<id>/report',CourseReportView.as_view()),
  path('course/<id>/users',AddUserToCourse.as_view()),

  #trainee
  path('course/<int:id>/comments',ListCreateCommentView.as_view()),
  path('course/<id>/comments/reply',CreateReplyView.as_view()),
  



  path('mark-content-completed' , MarkContentView.as_view()),
  path('trainee/course/<id>/dashboard',TraineeCourseDashboard.as_view()),
  
]

 