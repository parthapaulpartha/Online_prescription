from django import forms
from django.forms import TextInput
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import prescription


# -------- Registration ----------
class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
        ]

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user

# -------- Login ----------
class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)

# -------- EditProfile ----------
class EditprofileForm(UserChangeForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
        ]

# ---------- PrescriptionForm -----------
class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = prescription
        fields = [
            'hospital_name',
            # 'doctor_name',
            'doctor_type',
            'doctor_phone',
            'doctor_email',
            'doctor_designation',
            'patient_name',
            'gender',
            'age',
            'disease',
            'diagnosis',
            'treatment_planning',
            'next_visit_date',
            'doctor_signature',
        ]