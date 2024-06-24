from django.contrib import admin
from system.models.admin import Admin
from system.models.Admin_Contract import Admin_Contract
from system.models.Admin_Notfication import Admin_Notfication
from system.models.owner import Owner
from system.models.Owner_Notfication import Owner_Notfication
from system.models.trainer import Trainer
from system.models.Trainer_Contract import Trainer_Contract
from system.models.Trainer_Notfication import Trainer_Notfication
from system.models.trainee import Trainee
from system.models.Trainee_Contract import Trainee_Contract
from system.models.Trainee_Notfication import Trainee_Notfication
from system.models.Company import Company
from system.models.Planes import Planes
from system.models.Company_Planes import Company_Planes
from system.models.Course import Course
from system.models.Unit import Unit
from system.models.Content import Content
from system.models.Pdf import Pdf
from system.models.Video import Video
from system.models.Test import Test
from system.models.Question import Question
from system.models.Answer import Answer
from system.models.Edit_unit import EditUnit
from system.models.Edit_pdf import EditPdf
from system.models.Edit_Video import EditVideo

# Register your models here.
admin.site.register(Admin)
admin.site.register(Admin_Contract)
admin.site.register(Admin_Notfication)
admin.site.register(Owner)
admin.site.register(Owner_Notfication)
admin.site.register(Trainer)
admin.site.register(Trainer_Contract)
admin.site.register(Trainer_Notfication)
admin.site.register(Trainee)
admin.site.register(Trainee_Contract)
admin.site.register(Trainee_Notfication)
admin.site.register(Company)
admin.site.register(Company_Planes)
admin.site.register(Planes)

admin.site.register(Course)
admin.site.register(Unit)
admin.site.register(Content)
admin.site.register(Pdf)
admin.site.register(Video)
admin.site.register(Test)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(EditUnit)
admin.site.register(EditPdf)
admin.site.register(EditVideo)