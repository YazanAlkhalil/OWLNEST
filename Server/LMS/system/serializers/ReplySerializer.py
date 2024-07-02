#DRF 
from rest_framework import serializers

#models 
from system.models.Reply import Reply



class ReplySerializer(serializers.ModelSerializer):

      class Meta:
            model = Reply
            fields = '__all__'