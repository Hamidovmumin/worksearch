from django.contrib import admin
from vacancies.models import Vacancy,Category,WorkType


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ('vacancy_name', 'category_vacancy','company_name','company_email','location_work')
    search_fields = ('category_vacancy', 'company_name')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','style')
    prepopulated_fields = {'slug':('name',)}

@admin.register(WorkType)
class WorkTypeAdmin(admin.ModelAdmin):
    list_display = ('type','style')