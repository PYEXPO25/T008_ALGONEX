from django.contrib import admin
from .models import NurseProfile, PatientProfile
# Register your models here.


admin.site.register(NurseProfile)
admin.site.register(PatientProfile)