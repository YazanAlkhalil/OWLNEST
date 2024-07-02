#DRF 
from rest_framework import serializers

#models 
from system.models.Comment import Comment
from system.models.Course import Course

#django 
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

#serializers 
from system.serializers.ReplySerializer import ReplySerializer

class CommentSerializer(serializers.ModelSerializer):
    replies = ReplySerializer(source = "reply_set",read_only = True , many = True)
    class Meta:
        model = Comment
        fields = ["id", "content","user","replies","likes","dislikes"]
        extra_kwargs = {"user": {"read_only": True},"likes":{"read_only": True},"dislikes":{"read_only": True}}

    def create(self, validated_data):
        course = get_object_or_404(Course, id=self.context['view'].kwargs['id'])
        user = get_object_or_404(get_user_model(), id=self.context['request'].user.id)
        obj = Comment.objects.create(course=course, user=user, **validated_data)
        return obj
    
    def to_representation(self, instance):
        data = super().to_representation(instance) 
        data["image"] =  getattr(instance.user, 'image', None) or None
        return data