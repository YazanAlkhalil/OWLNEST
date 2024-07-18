from django.db import models 
#models 
from authentication.models.User import User
from system.models.Company import Company

#utils 
from django.utils import timezone
class Notification(models.Model):
      from_user = models.ForeignKey(User,related_name="noti",on_delete=models.CASCADE)
      to_user = models.ForeignKey(User,related_name="notification",on_delete=models.CASCADE)
      company = models.ForeignKey(Company,on_delete=models.CASCADE)
      sent_at = models.DateTimeField(auto_now_add=True)
      message = models.TextField()
      is_read = models.BooleanField(default=False)

      def time_since_sent(self):
        return timezone.now() - self.sent_at