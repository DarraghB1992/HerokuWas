from django.forms import ModelForm
from .models import ContactModel
from django import forms


class ContactView(ModelForm):
    message = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = ContactModel
        fields = ('name', 'email', 'topic', 'message')