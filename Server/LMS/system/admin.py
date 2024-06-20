from django.contrib import admin
from system.models.Admin import Admin
from system.models.Admin_Contract import Admin_Contract
from system.models.Admin_Notfication import Admin_Notfication
from system.models.Owner import Owner
from system.models.Owner_Notfication import Owner_Notfication
from system.models.Trainer import Trainer
from system.models.Trainer_Contract import Trainer_Contract
from system.models.Trainer_Notfication import Trainer_Notfication
from system.models.Trainee import Trainee
from system.models.Trainee_Contract import Trainee_Contract
from system.models.Trainee_Notfication import Trainee_Notfication
from system.models.Company import Company
from system.models.Planes import Planes
from system.models.Company_Planes import Company_Planes

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
