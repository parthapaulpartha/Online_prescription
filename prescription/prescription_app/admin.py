from django.contrib import admin
from .models import slider_images, prescription

# Register your models here.
admin.site.site_header = 'Prescription'

admin.site.register(slider_images)

class PrescriptionAdmin(admin.ModelAdmin):
    list_display = 'doctor_name', 'doctor_type', 'patient_name', 'date', 'age', 'gender',
    list_filter = 'doctor_name', 'doctor_type', 'patient_name', 'date', 'age', 'gender',
    search_fields = 'patient_name',
admin.site.register(prescription, PrescriptionAdmin)
