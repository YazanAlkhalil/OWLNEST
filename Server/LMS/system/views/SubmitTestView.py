#DRF 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
#models  
from system.models.Enrollment import Enrollment
from system.models.Content import Content
from system.models.Grade import Grade
from system.models.Test import Test
from system.models.Question import Question
from system.models.Answer import Answer

from decimal import Decimal
from django.shortcuts import get_object_or_404

class SubmitTestView(APIView):
      permission_classes = [IsAuthenticated]

      def post(self,request,test_id,course_id):
          test = get_object_or_404(Test,id = test_id)
          trainee_questions = request.data.get('questions')
          response = []
          enrollment = Enrollment.objects.get(course = course_id, trainee_contract__trainee__user = request.user)
          gained_xp = 0
          test.full_mark = 0
          test.save()
          if test.id in [grade.test.id for grade in enrollment.grade_set.all()]:
              enrollment.grade_set.get(test = test).delete()

          total = 0
          for question in trainee_questions:
               
               q = Question.objects.get(id = question["id"])
               passed = True
               answers = []
               
               
                   
               for answer in q.answer_set.all():
                   a = Answer.objects.get(id = answer.id)
                   
                   if not (len(question["answers"]) == Answer.objects.filter(question = q,is_correct = True).count()):
                        passed = False
                   
                   answers.append({
                        "id":a.id,
                        "text":a.answer,
                        "is_correct":a.is_correct
                   })

               for answer in question["answers"]:
                   a = Answer.objects.get(id = answer)
                   if not a.is_correct:
                       passed = False
                       break
              
               if passed: 
                  total += q.mark
                  print(total)
               response.append({
                         "id":q.id,
                         "question":q.question,
                         "mark":q.mark,
                         "feedback": "" if passed else q.feedback,
                         "passed":passed, 
                    }) 
               
               test.full_mark += q.mark 
               test.save()  
          score  = total/test.full_mark *100
          gained_xp =  score
          grade = Grade.objects.create(test = test,enrollment = enrollment , score = score , xp = gained_xp)
          data = {
              "questions":response,
              "score":grade.score
          }
          return Response(data,200)    
                
             












 