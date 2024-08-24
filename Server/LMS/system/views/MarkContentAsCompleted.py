#DRF 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
#models  
from system.models.Enrollment import Enrollment
from system.models.Content import Content
from system.models.Finished_Content import Finished_Content
from system.models.Grade import Grade
from system.models.Certificate import Certificate
#serializers 
from system.serializers.MarkContentSerializer import MarkContentSerializer
from rest_framework.permissions import IsAuthenticated
#django
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from django.conf import settings
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont
import os 


class MarkContentView(APIView):
      serializer_class = MarkContentSerializer
      permission_classes = [IsAuthenticated]
      def post(self, request, *args, **kwargs): 
                enrollment = get_object_or_404(Enrollment, trainee_contract__trainee__user=request.user, course__id=kwargs["id"])
                content = get_object_or_404(Content, id=kwargs["content_id"])
                if enrollment.course != content.unit.course:
                    return Response({"message": "You can't mark content if you are not enrolled in this course"}, status=status.HTTP_400_BAD_REQUEST)
                
                if content.id in [finished_content.content.id for finished_content in enrollment.finished_content_set.all()]:
                    return Response({"message": "You already marked it as completed"}, status=200)
                
                # Mark the content as finished
                Finished_Content.objects.create(enrollment=enrollment, content=content)
                 
                if enrollment.progress == 100 and not enrollment.completed:
                    passed = all(grade.score >= 60 for grade in enrollment.grade_set.all())
                    
                    if passed:
                        enrollment.completed = True
                        enrollment.completed_at = timezone.now()
                        enrollment.save(update_fields=['completed', 'completed_at'])  
                        
                        certificate_image = self.generate_certificate_image(enrollment)
                        certificate_image = certificate_image.split(sep='static\\')[1]
                        Certificate.objects.create(trainee_contract= enrollment.trainee_contract, certificate=certificate_image)
                        
                        return Response({"status": "passed"}, status=status.HTTP_200_OK)
                
                return Response({"message": "Completed","enrollment_progress":enrollment.progress}, status=status.HTTP_200_OK)

 
      def generate_certificate_image(self, enrollment):
          # Set up image dimensions and colors
          image_width = 1200
          image_height = 850
          background_color = "#FFFFFF"# White background
          text_color = "#333333"# Dark gray text
          border_color = "#4CAF50"# Green border
          accent_color = "#FFA500"# Accent color for decorative elements
          secondary_accent_color = "#1E88E5"# Blue accent for additional contrast
          margin = 60# Increased margin for a more spacious design# Create image object with borders
          image = Image.new("RGB", (image_width, image_height), color=border_color)
          draw = ImageDraw.Draw(image)
          inner_image = Image.new("RGB", (image_width - 2 * margin, image_height - 2 * margin), color=background_color)
          image.paste(inner_image, (margin, margin))

          # Add a subtle gradient to the background
          for i in range(image_height - 2 * margin):
              gradient_color = (245 - i // 10, 245 - i // 10, 245 - i // 10)  # Soft gradient effect
              gradient = Image.new('RGB', (image_width - 2 * margin, 1), gradient_color)
              image.paste(gradient, (margin, margin + i))

          # Load fonts (adjust paths if necessary)
          title_font = ImageFont.truetype("arial.ttf", 80)
          subtitle_font = ImageFont.truetype("arial.ttf", 55)
          text_font = ImageFont.truetype("arial.ttf", 40)
          watermark_font = ImageFont.truetype("arial.ttf", 30)
          grade_font = ImageFont.truetype("arialbd.ttf", 50)  # Bold font for grade
          logo_font = ImageFont.truetype("arialbd.ttf", 36)  # Font for OwlNest and company name# Helper function to calculate text size
          def get_text_size(text, font):
              bbox = draw.textbbox((0, 0), text, font=font)
              return bbox[2] - bbox[0], bbox[3] - bbox[1]  # width, height# Title
          title_text = "Certificate of Completion"
          title_width, title_height = get_text_size(title_text, title_font)
          title_x = (image_width - title_width) // 2
          title_y = 100
          draw.text((title_x, title_y), title_text, font=title_font, fill="#4CAF50")  # Green color# Trainee Name
          name_text = f"Congratulations, {enrollment.trainee_contract.trainee.user.username}!"
          name_width, name_height = get_text_size(name_text, subtitle_font)
          name_x = (image_width - name_width) // 2
          name_y = title_y + title_height + 50
          draw.text((name_x, name_y), name_text, font=subtitle_font, fill=text_color)

          # Course Name
          course_text = f"For Successfully Completing the Course: {enrollment.course.name}"
          course_width, course_height = get_text_size(course_text, text_font)
          course_x = (image_width - course_width) // 2
          course_y = name_y + name_height + 40
          draw.text((course_x, course_y), course_text, font=text_font, fill=text_color)

          # Date
          date_text = f"Date: {enrollment.completed_at.strftime('%Y-%m-%d')}"
          date_width, date_height = get_text_size(date_text, text_font)
          date_x = (image_width - date_width) // 2
          date_y = course_y + course_height + 40
          draw.text((date_x, date_y), date_text, font=text_font, fill=text_color)

          # Grade
          grades = enrollment.grade_set.all()
          avg_grade = sum(grade.score for grade in grades) / len(grades) if grades else 0
          grade_text = f"Grade: {avg_grade:.2f}"
          grade_width, grade_height = get_text_size(grade_text, grade_font)
          grade_x = (image_width - grade_width) // 2
          grade_y = date_y + date_height + 50
          draw.text((grade_x, grade_y), grade_text, font=grade_font, fill="#D32F2F")  # Red color for emphasis# Add a decorative line with accents
          line_start_x = margin + 100
          line_start_y = grade_y + grade_height + 60
          line_end_x = image_width - margin - 100
          line_end_y = line_start_y
          draw.line([(line_start_x, line_start_y), (line_end_x, line_end_y)], fill=accent_color, width=5)

          # OwlNest Name
          owlnest_text = "OwlNest"
          owlnest_width, owlnest_height = get_text_size(owlnest_text, logo_font)
          owlnest_x = (image_width // 4) - (owlnest_width // 2)
          owlnest_y = line_start_y + 50
          draw.text((owlnest_x, owlnest_y), owlnest_text, font=logo_font, fill=secondary_accent_color)

          # Company Name
          company_text = enrollment.course.company.name
          company_width, company_height = get_text_size(company_text, logo_font)
          company_x = (image_width * 3 // 4) - (company_width // 2)
          company_y = line_start_y + 50
          draw.text((company_x, company_y), company_text, font=logo_font, fill=secondary_accent_color)

          # Add a seal or decorative emblem (optional)
          seal_radius = 70
          seal_center = (image_width - seal_radius * 2 - 80, image_height - seal_radius * 2 - 80)
          draw.ellipse([seal_center, (seal_center[0] + seal_radius * 2, seal_center[1] + seal_radius * 2)], fill="#FFD700", outline=accent_color, width=8)
          seal_text = "Certified"
          seal_text_width, seal_text_height = get_text_size(seal_text, watermark_font)
          draw.text((seal_center[0] + seal_radius - seal_text_width // 2, seal_center[1] + seal_radius - seal_text_height // 2), seal_text, font=watermark_font, fill="#333333")

         # Path for saving the certificate
          certificate_dir = os.path.join(settings.MEDIA_ROOT, 'certifications')
          if not os.path.exists(certificate_dir):
              os.makedirs(certificate_dir, exist_ok=True)
              print(f"Created directory: {certificate_dir}")

          certificate_filename = f"certificate_{enrollment.trainee_contract.trainee.user.username}_{enrollment.course.name}.png"
          certificate_path = os.path.join(certificate_dir, certificate_filename)
          
          # Check if the path is correct
          print(f"Saving certificate to: {certificate_path}")
          
          # Save the certificate image
          try:
             image.save(certificate_path)
             print(f"Certificate saved successfully to {certificate_path}")
          except Exception as e:
              print(f"Error saving certificate: {e}")

          return certificate_path