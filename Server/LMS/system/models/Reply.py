from django.db import models 
from authentication.models.User import User
from system.models.Course import Course
class Reply(models.Model):
      user = models.ForeignKey(User,on_delete=models.CASCADE)
      course = models.ForeignKey(Course,on_delete=models.CASCADE)
      content = models.TextField(max_length = 1024)
      likes = models.IntegerField()
      dislikes = models.IntegerField()
      