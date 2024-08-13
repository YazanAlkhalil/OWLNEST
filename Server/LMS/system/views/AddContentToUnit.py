#DRF
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError
#models 
from system.models.DraftUnit import DraftUnit 
#serializer 
from system.serializers.DraftContentSerializer import DraftContentserializer
from system.serializers.DraftPDFSerializer import DraftPDFSerializer
from system.serializers.DraftVideoSerializer import DraftVideoSerializer
from system.serializers.DraftTestSerializer import DraftTestSerializer
from system.serializers.DraftAnswerSerializer import DraftAnswerSerializer
from system.serializers.DraftQuestionSerializer import DraftQuestionSerializer
#django 
from django.shortcuts import get_object_or_404

class AddContentToUnit(CreateAPIView):
      serializer_class = DraftContentserializer
      permission_classes = [IsAuthenticated]

      def post(self, request, *args, **kwargs):
          if not( "title" in request.data.keys()):
              raise ValidationError({"message":"Please Enter the content title"}) 
          if not( "order" in request.data.keys()):
               raise ValidationError({"message":"Please Enter the content order"}) 
          if not( "type" in request.data.keys()):
               raise ValidationError({"message":"Please Enter the content type"})
          unit = get_object_or_404(DraftUnit,id = kwargs["unit_id"])
          type = request.data["type"]
          data = {
                  "title":request.data["title"],
                  "order":request.data["order"],
                   
             }
          if type.lower() == "pdf": 
             serialized_content = DraftContentserializer(data = data)
             serialized_content.is_valid(raise_exception=True)
             content = serialized_content.save(unit = unit,is_pdf = True)
             pdf_data = {
                  "file":request.data["file"]
             }
             serialized_pdf = DraftPDFSerializer(data = pdf_data)
             serialized_pdf.is_valid(raise_exception=True)
             serialized_pdf.save(content = content)
             return Response({"message":"the pdf uploaded successfully"},201)
          
          if type.lower() == "video":
             serialized_content = DraftContentserializer(data = data)
             serialized_content.is_valid(raise_exception=True)
             content = serialized_content.save(unit = unit,is_video = True)
             pdf_data = {
                  "file":request.data["file"]
             }
             serialized_pdf = DraftVideoSerializer(data = pdf_data)
             serialized_pdf.is_valid(raise_exception=True)
             serialized_pdf.save(content = content)
             return Response({"message":"the video uploaded successfully"},201)
          if type.lower() == "quizz":
             serialized_content = DraftContentserializer(data = data)
             serialized_content.is_valid(raise_exception=True)
             content = serialized_content.save(unit = unit,is_test = True)
            
             serialized_test = DraftTestSerializer(data = {})
             serialized_test.is_valid(raise_exception=True)
             test = serialized_test.save(content = content)

             questions = request.data["questions"]
             
             for question in questions:
                 question_data = {
                     "question": question["question"],
                     "feedback": question["feedback"],
                     "mark": question["mark"],
                 }
                 serialized_question = DraftQuestionSerializer(data = question_data)
                 serialized_question.is_valid(raise_exception= True)
                 question_obj = serialized_question.save(quizz = test)
                 
                 for answer in question["answers"]:
                     answer_data = {
                         "answer":answer["answer"],
                         "is_correct":answer["is_correct"]
                     }
                     serialized_answer = DraftAnswerSerializer(data = answer_data)
                     serialized_answer.is_valid(raise_exception=True)
                     serialized_answer.save(question = question_obj)
             return Response({"message":"the quizz added to the course"})
          return Response({"message":"please add Video , PDF or Test"})

                 


             
               

