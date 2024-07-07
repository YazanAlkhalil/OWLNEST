from django.db import models 
from authentication.models.User import User
from system.models.Comment import Comment
class Reply(models.Model):
      user = models.ForeignKey(User,on_delete=models.CASCADE)
      comment = models.ForeignKey(Comment,on_delete=models.CASCADE, default=None )
      content = models.TextField(max_length = 1024)
      likes = models.IntegerField(null= True ,blank = True)
      dislikes = models.IntegerField(null=True,blank=True)
      created_at = models.DateTimeField(auto_now_add=True)
      def __str__(self) -> str:
            return f"{self.user.username} || {self.content}"  
      
      
      class Meta:
        ordering = ['-created_at']