from .models import user
from django import forms

class UserForm(forms.ModelForm):
    class Meta:
        model = user
        fields = '__all__'