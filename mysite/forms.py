from django import forms
from .models import Contact

class NewForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ['email', 'subject','message']

