from django.urls import path
from cv.views import resume_step

app_name = 'cv'

urlpatterns = [
    path('step/', resume_step, name='cv'),
]