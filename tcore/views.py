from django.shortcuts import render
from vacancies.models import Vacancy
from django.db.models import Q

def index(request):
    vacancy=Vacancy.objects.all().select_related('type_work')[::-1]

    context = {
        'vacancy': vacancy,
    }
    return render(request, 'index.html',context)

def search(request):
    search1 = request.GET.get('keyword1')
    search2 = request.GET.get('keyword2')
    vacancy = Vacancy.objects.all()

    if search1 or search2:
        query = Q()
        if search1:
            query &= Q(vacancy_name__icontains=search1)
        if search2:
            query &= Q(location_work__icontains=search2)
        vacancy = vacancy.filter(query)

    context = {
        'vacancy': vacancy,
        'search1': search1,
        'search2': search2,
    }

    return render(request, 'index.html',context)
