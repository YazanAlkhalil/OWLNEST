from django.db import models 
from system.models.Course import Course 
from authentication.models.User import User

class Comment(models.Model):
      user = models.ForeignKey(User,on_delete=models.CASCADE)
      course = models.ForeignKey(Course,on_delete=models.CASCADE)
      content = models.TextField()
      likes = models.ManyToManyField(User,related_name="likes",blank = True)
      dislikes = models.ManyToManyField(User,related_name='dislikes',blank=True)
      
      def __str__(self) -> str:
            return f"{self.user.username}  {self.content[0:10]}"