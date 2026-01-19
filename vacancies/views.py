from django.shortcuts import render,get_object_or_404
from django.db.models import Count
from vacancies.models import Vacancy,Category
from django.core.paginator import Paginator
from django.utils import timezone

def vacancies(request,id=None):
    count = Vacancy.objects.all().count()
    if id == None:
        vacancy_all = Vacancy.objects.all().select_related('category_vacancy')
        # select_related('category_vacancy')- Vakansiyanı götürəndə onun kategoriyasını da eyni sorğu ilə götür.
        category_all = Category.objects.annotate(vacancy_count=Count('vacancies_count'))
        paginator = Paginator(vacancy_all, 9)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
    else:
        category = get_object_or_404(Category, id=id)
        vacancy_all = Vacancy.objects.filter(category_vacancy_id=category)[::-1]
        paginator = Paginator(vacancy_all, 6)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        category_all = Category.objects.annotate(vacancy_count=Count('vacancies_count'))

    context = {
        'category': category_all,
        'vacancy': paged_products,
        'count': count,
    }
    return render(request, 'vacancies/vacancies.html',context)


def vacancy_detail(request,id):
    vacancy = get_object_or_404(Vacancy, id=id)
    if vacancy.views == 0:
        vacancy.views = 1
    else:
        vacancy.views +=1
    vacancy.save()
    view =vacancy.views


    category = Category.objects.get(id=vacancy.category_vacancy_id)
    vacancy_by_category = Vacancy.objects.filter(category_vacancy_id=category).exclude(id=vacancy.id)
    # exclude Django ORM funksiyasıdır(QuerySet metodu). Sadə dillə desək: filtrdən müəyyən şərtə
    # uyğun olanları ÇIXARIR.

    today=timezone.now().date()
    context = {
        'vacancy': vacancy,
        'view': view,
        'vacancy_by_category': vacancy_by_category,
        'today': today,
    }

    return render(request, 'vacancies/vacancy_detail.html',context)


