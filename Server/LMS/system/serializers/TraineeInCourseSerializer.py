# serializers.py
from rest_framework import serializers 

#models 
from system.models.Enrollment import Enrollment 
#django 
from django.db.models import Avg ,Sum
class TraineesInCourseSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    total_xp = serializers.SerializerMethodField()
    avg_grade = serializers.SerializerMethodField()
    completed_at = serializers.DateField()
    progress = serializers.FloatField()
    
    class Meta:
        model = Enrollment
        fields = ['name', 'total_xp', 'avg_grade', 'completed_at', 'progress']

    def get_name(self, obj):
        return f"{obj.trainee_contract.trainee.user.username}"

    def get_total_xp(self, obj):
        finished_content_xp = obj.finished_content_set.count() * 10
        grades_xp = obj.grade_set.aggregate(Sum('xp')).get('xp__sum') or 0
        return finished_content_xp + grades_xp

    def get_avg_grade(self, obj):
        return obj.grade_set.aggregate(Avg('score')).get('score__avg')
