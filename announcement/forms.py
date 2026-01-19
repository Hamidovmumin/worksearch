from django import forms
from vacancies.models import Vacancy

class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = '__all__'


    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['vacancy_name'].widget.attrs['placeholder'] = 'Enter vacancy_name number'
