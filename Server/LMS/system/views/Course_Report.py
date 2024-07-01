#DRF imports 
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

#django 
from django.shortcuts import get_object_or_404



class CourseReport(APIView): 
      def get(self,request,*args,**kwargs):
            pass