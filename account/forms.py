from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ( "email", "realstate", "image", "address", "telephone", "website", "instagram", "whatsapp" )