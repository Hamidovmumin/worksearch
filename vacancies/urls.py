from django.urls import path
from vacancies.views import vacancies,vacancy_detail

app_name = 'vacancies'

urlpatterns = [
    path('', vacancies, name='vacancies'),
    path('<int:id>/', vacancies, name='vacancies_by_category'),

    path('vacancy_detail/<int:id>/', vacancy_detail, name='vacancy_detail'),
]