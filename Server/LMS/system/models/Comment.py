from django.db import models 
from system.models.Course import Course 
from authentication.models.User import User

class Comment(models.Model):
      user = models.ForeignKey(User,on_delete=models.CASCADE)
      course = models.ForeignKey(Course,on_delete=models.CASCADE)
      content = models.TextField()
      likes = models.IntegerField()
      dislikes = models.IntegerField()
      
      def __str__(self) -> str:
            return f"{self.user.name}  {self.content[0:10]}"