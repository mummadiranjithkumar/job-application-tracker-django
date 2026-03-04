from django import forms
from .models import JobApplication


class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = [
            "company",
            "role",
            "location",
            "application_date",
            "status",
            "notes",
        ]
        widgets = {
            "application_date": forms.DateInput(attrs={"type": "date"}),
        }
