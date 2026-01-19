from django.urls import path
from announcement.views import announcement

app_name = 'announcement'

urlpatterns = [
    path('', announcement, name='announcement'),
]