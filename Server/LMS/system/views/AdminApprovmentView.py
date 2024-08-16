#DRF
from rest_framework.response import Response
from rest_framework.views import APIView 
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError
#models 
from system.models.Company import Company
from system.models.Course import Course
from system.models.Company_Planes import Company_Planes
from system.models.Courses_In_Plane import Courses_In_Plane
#serializers 
from system.serializers.SkillSerializer import SkillSerializer
from system.serializers.UnitSerializer import UnitSerializer 
from system.serializers.ContentSerializer import ContentSerializer
from system.serializers.PDFSerializer import PDFSerializer
from system.serializers.TestSerializer import TestSerializer
from system.serializers.QuestionSerializer import QuestionSerializer
from system.serializers.AnswerSerializer import AnswerSerializer
from system.serializers.VideoSerializer import VideoSerializer
from system.serializers.AdditionalResourceSerializer import AdditionalResourceSerializer
#django 
from django.shortcuts import get_object_or_404
# permissions 
from ..permissions.Plane import DoesHaveAPlane

class AdminApprovmentView(APIView):
      permission_classes = [IsAuthenticated, DoesHaveAPlane]
      def post(self, request, *args, **kwargs):
          company_id = self.kwargs['company_id']
          course = get_object_or_404(Course,id = kwargs["course_id"])
          for unit in  course.unit_set.all():
              for content in unit.content_set.all():
                  content.delete()
              unit.delete()
          course.skill_set.all().delete()
          if hasattr(course , "resource"):
              course.resource.delete()
          course.published = True
          
          #skills
          for skill in course.draftskill_set.all():
              skill_data = {
                   "skill":skill.skill,
                   "rate":skill.rate
              }
              serialized_skill = SkillSerializer(data = skill_data)
              serialized_skill.is_valid(raise_exception=True)
              serialized_skill.save(course = course)
          
          #additional resources 
          if hasattr(course, 'draftadditionalresources'):
             serialized_resource = AdditionalResourceSerializer(data = {"text":course.draftadditionalresources.text})
             serialized_resource.is_valid(raise_exception=True)
             serialized_resource.save(course = course)
          #units and contents 
          for unit in course.draft_units.all():
               unit_data = {
                    "title":unit.title,
                    "order":unit.order
               }
               serialized_unit = UnitSerializer(data = unit_data)
               serialized_unit.is_valid(raise_exception=True)
               unit_obj =  serialized_unit.save(course = course)

               for content in unit.contents.all():
                   content_data = { 
                        "title":content.title,
                        "order":content.order
                   }
                   serialized_content = ContentSerializer(data=content_data)
                   serialized_content.is_valid(raise_exception=True)
                   content_obj = serialized_content.save(unit = unit_obj)
                   if content.is_pdf:
                      content_obj.is_pdf = True
                      content_obj.save()
                      pdf = content.draftpdf
                      pdf_data = {
                          "file_path":pdf.file
                      }
                      serialized_pdf = PDFSerializer(data = pdf_data)
                      serialized_pdf.is_valid(raise_exception=True)
                      serialized_pdf.save(content = content_obj)

                   if content.is_video:
                      content_obj.is_video = True
                      content_obj.save()
                      video = content.draftvideo
                      video_data = {
                            "file_path":video.file,
                            "description":video.description
                      }
                      serialized_video = VideoSerializer(data = video_data)
                      serialized_video.is_valid(raise_exception=True)
                      serialized_video.save(content = content_obj)
                   
                   if content.is_test:
                      content_obj.is_test = True
                      content_obj.save()
                      drafttest = content.drafttest 
                      serialized_test = TestSerializer(data = {})
                      serialized_test.is_valid(raise_exception=True)
                      test = serialized_test.save(content = content_obj)
                      
                      for question in drafttest.draftquestion_set.all(): 
                          question_data = {
                              "question":question.question,
                              "feedback":question.feedback,
                              "mark":question.mark
                          }

                          serialized_question = QuestionSerializer(data = question_data)
                          serialized_question.is_valid(raise_exception=True)
                          question_obj = serialized_question.save(test = test)
                          for answer in question.draftanswer_set.all():
                              answer_data = {
                                  "answer":answer.answer,
                                  "is_correct":answer.is_correct
                              }
                              serialized_answer = AnswerSerializer(data = answer_data)
                              serialized_answer.is_valid(raise_exception=True)
                              serialized_answer.save(question = question_obj)
          course.save() 
          course_added_to_a_plane = False
          # get the company planes
          company_planes = Company_Planes.objects.filter(company__id=company_id, is_active=True, is_full=False)
          if company_planes.__len__() > 0:
            for company_plane in company_planes:
                if not course_added_to_a_plane:
                    if company_plane.current_courses_number < company_plane.plane.courses_number:
                        courses_in_plane = Courses_In_Plane.objects.filter(company_plane=company_plane)
                        if courses_in_plane.__len__() > 0:
                            # if the course is in the courses in the plane then escape
                            if courses_in_plane.filter(course=course).exists():
                                break
                        # if the courses in plan is emplty or if the course does not exists in it then create the course in it
                        print('6')
                        course_in_plane = Courses_In_Plane.objects.create(company_plane=company_plane, course=course)
                        course_in_plane.save()
                        company_plane.current_courses_number += 1
                        if company_plane.current_courses_number == company_plane.plane.courses_number:
                            company_plane.is_full = True
                        company_plane.save()
                        course_added_to_a_plane = True
                    # when thid company does not have the capacity for another course
                    else:
                        continue
          else:
                raise ValidationError({'message': f'This Company Doesn\'t have an active plane, Purchase a new one'})
          print(request.user.admin.admin_contract_set.get(company = get_object_or_404(Company, id = kwargs["company_id"])).adminapprovment_set.get(course = course).delete())
          return Response({"message":"The course has been published successfully"})