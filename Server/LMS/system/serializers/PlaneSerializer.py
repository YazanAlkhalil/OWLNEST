from rest_framework import serializers
from system.models.Planes import Planes

from rest_framework import serializers
from system.models.Planes import Planes
from system.models.Company_Planes import Company_Planes
from datetime import timedelta

class PlaneSerializer(serializers.ModelSerializer):
    subscription_term = serializers.SerializerMethodField()

    class Meta:
        model = Planes
        fields = ('id', 'plane_name', 'subscription_term', 'courses_number', 'price', 'additional_course_price')

    def get_subscription_term(self, obj):
        # Assuming subscription_term is a timedelta object
        delta = obj.subscription_term
        if delta.days > 0:
            return f"{delta.days} day{'s' if delta.days > 1 else ''}"
        # elif delta.seconds < 60:
        #     return f"{delta.seconds} seconds"
        # elif delta.seconds < 3600:
        #     minutes = delta.seconds // 60
        #     return f"{minutes} minute{'s' if minutes > 1 else ''}"
        # elif delta.seconds < 86400:
        #     hours = delta.seconds // 3600
        #     return f"{hours} hour{'s' if hours > 1 else ''}"


class CompanyPlaneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company_Planes
        fields = ('id','plane','company','is_full','is_active','purchased_at')

