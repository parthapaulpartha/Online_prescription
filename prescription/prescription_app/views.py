from django.shortcuts import render, redirect, get_object_or_404

from .forms import (
    RegistrationForm,
    LoginForm,
    EditprofileForm,
    PrescriptionForm,
)

from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import (
        authenticate,
        login,
        logout,
        update_session_auth_hash,
)

from django.db.models import Q
from .models import slider_images, prescription

from django.contrib import messages


# Create your views here.

def home(request):
    all_slider_image = slider_images.objects.all()
    arg = {
        'images': all_slider_image
    }
    return render(request, 'prescription_app/home.html', arg)

# -------- Registration ------
def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Success! Your account signup successfully')
            return redirect('prescription/ragistration')

        else:
            messages.error(request, 'Please enter currenct informations')
            return redirect('prescription/registration')

    else:
        form = RegistrationForm()
        arg = {'form': form}
    return render(request, 'prescription_app/registration.html', arg)

# -------- Login ------
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if not user:
                messages.error(request, 'Username and Password did not matched')
                return redirect('prescription/login')
            login(request, user)
            return redirect('/prescription/home/')
    else:
        form = LoginForm()
        arg = {'form': form}
    return render(request, 'prescription_app/login.html', arg)

# -------- Logout ------
def logout_view(request):
    logout(request)
    return redirect('/prescription/login/')

# ------ Profile ---------
def profile(request):
    return render(request, 'prescription_app/profile.html')

# ------- Edit Profile -------
def edit_profile(request):
    if request.method == 'POST':
        form_u = EditprofileForm(request.POST, instance=request.user)
        if form_u.is_valid():
            form_u.save()
            messages.success(request, 'Profile Update successfully')
            return redirect('/prescription/profile/')
    else:
        form_u = EditprofileForm(instance=request.user)
        arg = {'form_u': form_u}
    return render(request, 'prescription_app/edit_profile.html', arg)

# -------- Change Password ---------
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Password Change Successfully')
            return redirect('/prescription/profile')
        else:
            messages.error(request, 'Did not match')
            return redirect('/prescription/change_password')

    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'prescription_app/change_password.html', args)

# ---------- Create_Prescription -------------
def create_prescription(request):
    if request.method == 'POST':
        form = PrescriptionForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.doctor_name = request.user
            instance.save()
    form = PrescriptionForm()
    arg = {
        'form': form
    }
    # hospital_name = request.POST.get("hospital_name")
    # doctor_name = request.user
    # doctor_type = request.POST.get('doctor_type')
    # doctor_phone = request.POST.get('doctor_phone')
    # doctor_email = request.POST.get('doctor_email')
    # doctor_designation = request.POST.get('doctor_designation')
    # patient_name = request.POST.get('patient_name')
    # gender = request.POST.get('gender')
    # age = request.POST.get('age')
    # date = request.POST.get('date')
    # disease = request.POST.get('disease')
    # diagnosis = request.POST.get('diagnosis')
    # treatment_planning = request.POST.get('treatment_planning')
    # next_visit_date = request.POST.get('next_visit_date')
    # doctor_signature = request.POST.get('doctor_signature')
    #
    # ption = prescription(hospital_name=hospital_name, doctor_name=doctor_name, doctor_type=doctor_type, doctor_phone=doctor_phone,
    #                      doctor_email=doctor_email, doctor_designation=doctor_designation, patient_name=patient_name, gender=gender,
    #                      age=age, date=date, disease=disease, diagnosis=diagnosis, treatment_planning=treatment_planning,
    #                      next_visit_date=next_visit_date, doctor_signature=doctor_signature)
    # ption.save()

    return render(request, 'prescription_app/create_prescription.html', arg)

def write_prescription(request):
    return render(request, 'prescription_app/write_prescription.html')

# ---------- search post -------
def search(request):
    if request.method == 'POST':
        search = request.POST['search']
        if search:
            match = prescription.objects.filter(Q(patient_name__icontains=search))

            if match:
                return render(request, 'prescription_app/search.html', {'sr': match})
            else:
                messages.error(request, 'No result found')
        else:
            return redirect('/prescription/search')

    return render(request, 'prescription_app/search.html')

# ---------- Prescription detail ---------
def prescription_detail(request, id, patient_name):
    prescription_info = prescription.objects.filter(id=id, patient_name=patient_name)

    arg = {
        'prescription_info': prescription_info,
    }
    return render(request, 'prescription_app/prescription_detail.html', arg)