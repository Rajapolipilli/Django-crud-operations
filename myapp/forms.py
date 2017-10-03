from django import forms
from .models import OrgList
from .models import EmpDetail
from .models import StatesList

class NewForm(forms.ModelForm):
    class Meta :
        model = OrgList
        fields =[
            'company_name',
            'company_logo',
            'company_website',
            'company_address',
            'company_state',
            #'slist',
        ]

class EmpForm(forms.ModelForm):
    class Meta :
        model = EmpDetail
        fields =[
            'orglist',
            'first_name',
            'last_name',
            'job_role'
        ]
