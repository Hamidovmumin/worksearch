from django.shortcuts import render,redirect
from companies.models import Company
from vacancies.models import Vacancy
from vacancies.models import Category
from django.db.models import Count


def companies(request):
    company = Company.objects.all()
    context = {
        'company': company,
    }
    return render(request, 'companies/companies.html',context)

def company_by_vacancy(request,id):
    count = Vacancy.objects.all().count()
    company = Company.objects.get(id=id)
    vacancy = Vacancy.objects.filter(company_name_id=company)
    category_all = Category.objects.annotate(vacancy_count=Count('vacancies_count'))
    context = {
        'vacancy': vacancy,
        'category': category_all,
        'count': count,
    }

    return render(request, 'vacancies/vacancies.html', context)