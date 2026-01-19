from django.urls import path,include
from payment.views import payment_form,pay,cancel,success
from .callback import callback

app_name = 'payment'

urlpatterns = [
    path('',payment_form,name='payment_form'),
    # path('pay/', pay, name='pay'),
    # path('success/', success, name='success'),
    # path('cancel/', cancel, name='cancel'),
    path("pay/", pay, name="pay"),

    # Click / eManat callback
    path("callback/", callback, name="callback"),

    # Nəticə səhifələri
    path("success/", success, name="success"),
    path("cancel/", cancel, name="cancel"),
]