# from django.shortcuts import render,redirect
# from vacancies.models import Vacancy
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from django.shortcuts import redirect
# from django.conf import settings
# import stripe
# import paypalrestsdk

# from django.urls import reverse
import uuid
from django.shortcuts import render, redirect
from django.conf import settings
import paypalrestsdk
from vacancies.models import Vacancy, Category, Company
from .models import Payment


# Create your views here.
def payment_form(request):
    if request.method == "POST":
        request.session['vacancy_data'] = {   # Session = istifadəçiyə məxsus gizli yaddaş,Brauzer bağlanana qədər qalır
            "vacancy_name": request.POST.get("vacancy_name"),
            "company_email": request.POST.get("company_email"),
            "company_name": request.POST.get("company_name"),
            "category_vacancy": request.POST.get("category_vacancy"),
            "type_work": request.POST.get("type_work"),
            "salary": request.POST.get("salary"),
            "salary_type": request.POST.get("salary_type"),
            "location_work": request.POST.get("location_work"),
            "vacancy_description": request.POST.get("vacancy_description"),
            "requirements": request.POST.get("requirements"),
            "deadline": request.POST.get("deadline"),
        }

        context ={
            'vacancy_name':request.POST.get("vacancy_name"),
            'location_work':request.POST.get("location_work"),
        }
        return render(request, "payment/payment.html",context)

    return redirect('/')




def payment_success(request):
    pass
    # if request.method == "POST":
    #     data = request.session.get("vacancy_data") # Session-dan məlumat oxunur
    #
    #     if not data:
    #         return JsonResponse({"status": "error", "message": "Session boşdur"})
    #
        # Vacancy.objects.create(
        #     vacancy_name=data["vacancy_name"],
        #     vacancy_description=data["vacancy_description"],
        #     requirements=data["requirements"],
        #     company_name_id=data["company_name"],
        #     category_vacancy_id=data["category_vacancy"],
        #     type_work_id=data["type_work"],
        #     company_email=data["company_email"],
        #     location_work=data["location_work"],
        #     salary=data["salary"],
        #     salary_type=data["salary_type"],
        #     deadline=data["deadline"],
        # )
    #
    #     del request.session["vacancy_data"] # Session təmizlənir
    #
    #     return JsonResponse({"status": "success"})
    #
    # return JsonResponse({"status": "error"})





# stripe.api_key = settings.STRIPE_SECRET_KEY
#
#
# def payment_page(request):
#     return render(request, "payment.html", {
#         "stripe_public_key": settings.STRIPE_PUBLIC_KEY
#     })
#
#
# @csrf_exempt
# def create_checkout_session(request):
#     session = stripe.checkout.Session.create(
#         payment_method_types=['card'],
#         line_items=[{
#             'price_data': {
#                 'currency': 'usd',
#                 'product_data': {
#                     'name': 'Elan yerləşdirmə',
#                 },
#                 'unit_amount': 1000,  # 10 USD
#             },
#             'quantity': 1,
#         }],
#         mode='payment',
#         success_url='http://127.0.0.1:8000/success/',
#         cancel_url='http://127.0.0.1:8000/cancel/',
#     )
#
#     return JsonResponse({'id': session.id})
#
#
# def success(request):
#     return render(request, "success.html")
#
# def cancel(request):
#     return render(request, "cancel.html")

####################################################

# def pay(request):
#
#     paypalrestsdk.configure({
#         "mode": settings.PAYPAL_MODE,
#         "client_id": settings.PAYPAL_CLIENT_ID,
#         "client_secret": settings.PAYPAL_CLIENT_SECRET
#     })
#
#     vacancy_data = request.session.get('vacancy_data')
#     if not vacancy_data:
#         return redirect('payment:payment_form')
#
#     payment = paypalrestsdk.Payment({
#         "intent": "sale",
#         "payer": {"payment_method": "paypal"},
#         "redirect_urls": {
#             "return_url": request.build_absolute_uri('/payment/success/'),
#             "cancel_url": request.build_absolute_uri('/payment/cancel/')
#         },
#         "transactions": [{
#             "amount": {
#                 "total": "6.00",
#                 "currency": "USD"
#             },
#             "description": "Vakansiya elanı"
#         }]
#     })
#
#     if payment.create():
#         for link in payment.links:
#             if link.rel == "approval_url":
#                 return redirect(link.href)
#
#     return render(request, 'payment/error.html', {"error": payment.error})
#
#
# def success(request):
#
#     paypalrestsdk.configure({
#         "mode": settings.PAYPAL_MODE,
#         "client_id": settings.PAYPAL_CLIENT_ID,
#         "client_secret": settings.PAYPAL_CLIENT_SECRET
#     })
#
#     payment_id = request.GET.get('paymentId')
#     payer_id = request.GET.get('PayerID')
#
#     payment = paypalrestsdk.Payment.find(payment_id)
#
#     if payment.execute({"payer_id": payer_id}):
#
#         # Payment save
#         Payment.objects.create(
#             payment_id=payment_id,
#             amount=10.00,
#             status="Success"
#         )
#
#         # Vakansiya save
#         data = request.session.get('vacancy_data')
#
#         # category = Category.objects.get(id=data['category_vacancy'])
#         # company = Company.objects.get(id=data['company_name'])
#         # type_work =
#
        # Vacancy.objects.create(
        #     vacancy_name=data["vacancy_name"],
        #     vacancy_description=data["vacancy_description"],
        #     requirements=data["requirements"],
        #     company_name_id=data["company_name"],
        #     category_vacancy_id=data["category_vacancy"],
        #     type_work_id=data["type_work"],
        #     company_email=data["company_email"],
        #     location_work=data["location_work"],
        #     salary=data["salary"],
        #     salary_type=data["salary_type"],
        #     deadline=data["deadline"],
        # )
#
#         del request.session['vacancy_data']
#
#         return render(request, 'payment/success.html')
#
#     return render(request, 'payment/error.html')
#
#
#
# def cancel(request):
#     return render(request, 'payment/cancel.html')



###############################




def pay(request):
    vacancy_data = request.session.get('vacancy_data')
    if not vacancy_data:
        return redirect('payment:payment_form')

    # Ödəniş üçün test ID
    payment_id = str(uuid.uuid4())
    amount = 10  # AZN, nümunə
    Payment.objects.create(payment_id=payment_id, amount=amount, status='pending')

    # Session-da payment_id saxla
    request.session['payment_id'] = payment_id

    # Test üçün sadəcə redirect səhifəsi
    return render(request, 'payment/redirect.html', {'payment_id': payment_id, 'amount': amount})



def success(request):
    return render(request, "payment/success.html")


def cancel(request):
    return render(request, "payment/cancel.html")