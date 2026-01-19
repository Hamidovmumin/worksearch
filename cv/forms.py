# forms.py
from django import forms


class Step1Form(forms.Form):
    vacancy = forms.CharField(label='Peşə və ya vəzifə')
    salary = forms.IntegerField(label='Gözlənilən maaş')
    specialty = forms.CharField(label='İxtisas')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update(
                {
                    'class': 'form-control custom-input',
                    'style': 'max-width:500px; max-height:50px;'
                 }
            )


class Step2Form(forms.Form):
    firstName = forms.CharField(label='Ad', max_length=50)
    lastName = forms.CharField(label='Soyad', max_length=50)
    fatherName = forms.CharField(label='Ata adı', max_length=50)
    brithDate = forms.DateField(
        label='Doğum tarixi',
        widget=forms.DateInput(attrs={'type': 'date'}),
        input_formats=['%d-%m-%Y']
    )
    GENDER_CHOICES = (
        ('male', 'Kişi'),
        ('female', 'Qadın'),
    )

    gender = forms.ChoiceField(
        choices=GENDER_CHOICES,
        widget=forms.RadioSelect,
        label="Cins"
    )

    city = forms.CharField(label='Yaşadığınız şəhər', max_length=50)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update(
                {
                    'class': 'form-control custom-input',
                    'style': 'max-width:400px; max-height:40px;'
                }
            )


class Step3Form(forms.Form):
    education = forms.CharField(label='Təhsil müəssisəsinin adı')
    specialty=forms.CharField(label='İxtisas adı')
    startDate=forms.DateField(
        label='Başlama tarixi.',
        widget=forms.DateInput(format='%d/%m/%Y', attrs={
            'type': 'date',
            'style': 'max-width:140px; max-height:50px;'
        }),
        input_formats=['%d/%m/%Y']
    )

    endDate=forms.DateField(
        label='Bitmə tarixi.',
        widget=forms.DateInput(format='%d/%m/%Y', attrs={
            'type': 'date',
            'style': 'max-width:140px; max-height:50px;'
        }),
        input_formats=['%d/%m/%Y']
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update(
                {
                    'class': 'form-control custom-input',
                }
            )


