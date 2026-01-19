from django.urls import path
from companies.views import companies,company_by_vacancy

app_name = 'companies'

urlpatterns = [
    path('', companies, name='companies'),
    path('<int:id>/', company_by_vacancy, name='company_by_vacancy'),
]