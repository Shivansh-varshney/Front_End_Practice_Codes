from django.contrib.auth.models import User
from django import forms

class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-input'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-input'}))

    class Meta:
        model = User
        fields = ['username','email']