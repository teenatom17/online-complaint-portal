from django import forms
from .models import Complaint, ContactMessage

# ===========================
# CONTACT FORM
# ===========================
class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']


# ===========================
# COMPLAINT FORM
# ===========================
class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ['name', 'email', 'phone', 'complaint_text']
