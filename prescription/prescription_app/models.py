from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# -------- slider image --------
class slider_images(models.Model):
    image = models.ImageField(upload_to='slider_images', default='')
    title = models.CharField(max_length=50, default='')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Slider Image'

# --------- Prescription ------------
class prescription(models.Model):
    hospital_name = models.CharField(max_length=100, default='')
    doctor_name = models.ForeignKey(User, on_delete=models.CASCADE)
    TYPE_CHOICES = (
        ('audiologist', 'Audiologist'),
        ('allergist', 'Allergist'),
        ('anesthesiologist', 'Anesthesiologist'),
        ('cardiologist', 'Cardiologist'),
        ('dentist', 'Dentist'),
        ('dermatologist', 'Dermatologist'),
        ('endocrinologist', 'Endocrinologist'),
        ('epidemiologist', 'Epidemiologist'),
        ('gynecologist', 'Gynecologist'),
        ('immunologist', 'Immunologist'),
        ('infectious disease specialist', 'Infectious Disease Specialist'),
        (' medical geneticist', ' Medical Geneticist'),
        ('science fiction', 'Science fiction'),
        ('microbiologist', 'Microbiologist'),
        ('neonatologist', 'Neonatologist'),
        ('neurologist', 'Neurologist'),
        ('neurosurgeon', 'Neurosurgeon'),
        ('obstetrician', 'Obstetrician'),
        ('oncologist', 'Oncologist'),
        ('orthopedic surgeon', ' Orthopedic Surgeon'),
        ('eNT specialist', ' ENT Specialist'),
        ('pediatrician', 'Pediatrician'),
        ('physiologist', 'Physiologist'),
        ('plastic surgeon', 'Plastic Surgeon'),
        ('podiatrist', 'Podiatrist'),
        ('psychiatrist', 'Psychiatrist'),
        ('radiologist', 'Radiologist'),
        ('rheumatologist', 'Rheumatologist'),
        ('surgeon', 'Surgeon'),
        ('urologist', 'Urologist'),
    )
    doctor_type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    doctor_phone = models.CharField(max_length=15, default='')
    doctor_email = models.EmailField(default='')
    doctor_designation = models.TextField(max_length=600, default='')

    patient_name = models.CharField(max_length=100, default='')
    TYPE_GENDER = (
        ('male', 'Male'),
        ('female', 'Female'),
    )
    gender = models.CharField(max_length=50, choices=TYPE_GENDER)
    age = models.IntegerField(default='')
    date = models.DateTimeField(auto_now_add=True)
    disease = models.TextField(max_length=300, default='')
    diagnosis = models.TextField(max_length=300, default='')
    treatment_planning = models.TextField(max_length=900, default='')

    next_visit_date = models.DateField(default='')
    doctor_signature = models.CharField(max_length=50, default='')