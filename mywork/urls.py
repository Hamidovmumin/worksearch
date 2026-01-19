"""
URL configuration for mywork project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tcore.urls')),
    path('vacancies/', include('vacancies.urls')),
    path('companies/', include('companies.urls')),
    path('announcement/', include('announcement.urls')),
    path('payment/',include('payment.urls')),
    path('contact/',include('contact.urls')),
    path('cv/',include('cv.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)\
  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
