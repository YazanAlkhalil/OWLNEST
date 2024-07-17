# rest_framework
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
# models
from ..models.Temp_unit import Temp_Unit
from ..models.Pdf import Pdf
from ..models.Video import Video
from ..models.Test import Test
# serialzers
from ..serializers.Temp_Content import Temp_Content_Serializer
# permissions
from ..permissions.IsCourseTrainer import IsCourseTrainer

# POST : api/trainer/company/:company_id/courses/:course_id/unit/:unit_id/content
class ContentCreate(generics.CreateAPIView):
    # set the serializer class
    serializer_class = Temp_Content_Serializer
    # set the permission class
    permission_classes = [IsAuthenticated, IsCourseTrainer]
    # save the cours to the temp_unit
    def perform_create(self, serializer):
        course_id = self.kwargs['course_id']
        temp_unit_id = self.kwargs['unit_id']
        temp_unit = Temp_Unit.objects.get(id=temp_unit_id, course__id=course_id)
        # Check the type of content and save accordingly
        content_type = self.request.data.get('content_type')
        if content_type == 'pdf':
            temp_content = serializer.save(temp_unit=temp_unit, state='PR', is_pdf=True)
            Pdf.objects.create(temp_content=temp_content, file_path=self.request.data.get('file_path'))
        elif content_type == 'video':
            temp_content = serializer.save(temp_unit=temp_unit, state='PR', is_video=True)
            Video.objects.create(temp_content=temp_content, file_path=self.request.data.get('file_path'), description=self.request.data.get('description'))
        elif content_type == 'test':
            temp_content = serializer.save(temp_unit=temp_unit, state='PR', is_test=True)
            Test.objects.create(temp_content=temp_content, full_mark=self.request.data.get('full_mark'))