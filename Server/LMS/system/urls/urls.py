from django.urls import path 
#views 
from system.views.CourseReportView import CourseReportView
from system.views.Comment import ListCreateCommentView

#DRF
 
urlpatterns = [
  path('course/<id>/report',CourseReportView.as_view()),
  path('course/<int:id>/comments',ListCreateCommentView.as_view())
]
 