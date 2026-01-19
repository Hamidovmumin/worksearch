from django.db import models
from companies.models import Company
from django.urls import reverse

SALARY_TYPE_CHOICES = [
    ('AZN', 'AZN'),
    ('ERO', 'ERO'),
    ('USD', 'USD'),
]

WORK_TYPE_CHOICES = [
    ('Full-time','Full-time'),
    ('Remote','Remote'),
    ('Hybrid','Hybrid'),
    ('Part-time','Part-time'),
]

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, default='')
    style = models.CharField(max_length=100)
    icons = models.CharField(max_length=100,default="")
    icon_color = models.CharField(max_length=100,default="")

    def vacancy_count(self):
        return self.vacancies_count.count()

    def __str__(self):
        return self.name

class WorkType(models.Model):
    type = models.CharField(max_length=100, choices=WORK_TYPE_CHOICES)
    style = models.CharField(max_length=100)

    def __str__(self):
        return self.type

class Vacancy(models.Model):
    vacancy_name = models.CharField(max_length=100)
    vacancy_description = models.TextField()
    requirements = models.TextField(default="",help_text='Hər tələbi yeni sətirdə yazın')
    category_vacancy = models.ForeignKey(Category, on_delete=models.CASCADE,related_name='vacancies_count')
    company_name = models.ForeignKey(Company, on_delete=models.CASCADE)
    company_email = models.EmailField()
    location_work = models.CharField(max_length=100)
    salary = models.CharField(max_length=100)
    salary_type = models.CharField(max_length=100, choices=SALARY_TYPE_CHOICES)
    type_work = models.ForeignKey(WorkType, on_delete=models.CASCADE)
    views = models.PositiveIntegerField(default=0)
    deadline = models.DateField(
        verbose_name="Son müraciət tarixi",
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.vacancy_name


