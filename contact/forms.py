from django import forms
from contact.models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['full_name', 'email','phone', 'subject', 'message']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control','required': 'required'}),
            'email': forms.EmailInput(attrs={'class': 'form-control','required': 'required'}),
            'phone': forms.TextInput(attrs={'class': 'form-control','required': 'required'}),
            'subject': forms.TextInput(attrs={'class': 'form-control','required': 'required'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 4,'required': 'required'}),
        }