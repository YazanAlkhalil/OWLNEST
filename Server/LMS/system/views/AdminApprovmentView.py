#DRF
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError


#models 
from system.models.Company import Company
from system.models.Course import Course

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






class AdminApprovmentView(APIView):
      def post(self, request, *args, **kwargs):
          course = get_object_or_404(Course,id = kwargs["course_id"])
          course.unit_set.all().delete()
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
          if hasattr(course, 'additional_resources'):
             serialized_resource = AdditionalResourceSerializer(data = {"text":course})
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
          print(request.user.admin.admin_contract_set.get(company = get_object_or_404(Company, id = kwargs["company_id"])).adminapprovment_set.get(course = course).delete())
          return Response({"message":"The course has been published successfully"})