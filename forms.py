from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class PatientSignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'profile_picture',
                  'address_line1', 'city', 'state', 'pincode']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.user_type = 'patient'
        if commit:
            user.save()
        return user

class DoctorSignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'profile_picture',
                  'address_line1', 'city', 'state', 'pincode']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.user_type = 'doctor'
        if commit:
            user.save()
        return user

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'profile_picture', 'address_line1', 'city', 'state', 'pincode']
