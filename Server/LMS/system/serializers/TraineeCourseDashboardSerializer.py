#DRF 
from rest_framework import serializers

#system models 
from system.models.Enrollment import Enrollment
from system.models.Grade import Grade


class TraineeCourseDashboardSerializer(serializers.Serializer):
    completion = serializers.DecimalField(max_digits=5, decimal_places=2)
    xp_avg = serializers.DecimalField(max_digits=5, decimal_places=2)
    quizzes = serializers.ListField()

    def to_internal_value(self, data):
        dashboard = {}
        enrollment = data['enrollment']
        
        dashboard["completion"] = enrollment.progress
        dashboard["xp_avg"] = enrollment.xp_avg
        
        grades = Grade.objects.filter(enrollment=enrollment)
        quizzes = [
            {
                "title": grade.test.content.title,
                "passed": grade.score > 60,
                "full_mark": grade.test.full_mark,
                "score": grade.score,
                "taken_at": grade.taken_at
            }
            for grade in grades
        ]
        dashboard["quizzes"] = quizzes

        return dashboard
 