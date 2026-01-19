from django.shortcuts import render,redirect
from announcement.forms import AnnouncementForm
from companies.models import Company
from vacancies.models import Vacancy, Category,WorkType


def announcement(request):
    vacancy = Vacancy.objects.all()
    category = Category.objects.all()
    work_type = WorkType.objects.all()
    company = Company.objects.all()
    context = {
        'vacancy': vacancy,
        'category': category,
        'work_type': work_type,
        'company': company,
    }
    return render(request, 'announcement/announcement.html',context)




