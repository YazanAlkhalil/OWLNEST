from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
# models
from ..models.Test import Test
# serialzers
from ..serializers.Test import TestSerializer
# permissions
from ..permissions.Trainer import IsTrainer, IsCompanyTrainer, IsCourseTrainer

##########################
#                        #
#                        #
#       Delete Test      #
#                        #
#                        #
##########################

# DELETE: api/admin/company/:company-id/courses/course-id/units/unit_id/tests/test_id
class DeleteTest(generics.DestroyAPIView):
    # set the serializer class
    serializer_class = TestSerializer
    # set the permission class
    permission_classes = [IsAuthenticated, IsTrainer, IsCompanyTrainer, IsCourseTrainer]
    # set the queryset
    queryset = Test.objects.all()