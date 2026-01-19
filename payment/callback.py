# from django.views.decorators.csrf import csrf_exempt
# from django.http import HttpResponse
#
#
# @csrf_exempt
# def payment_callback(request):
#     data = request.POST
#
#     order_id = data.get("order_id")
#     status = data.get("status")
#     transaction_id = data.get("transaction_id")
#
#     try:
#         payment = Payment.objects.get(order_id=order_id)
#
#         if status == "success":
#             payment.status = "success"
#             payment.transaction_id = transaction_id
#             payment.save()
#
#             # burada istəsən:
#             # payment.vacancy.is_paid = True
#             # payment.vacancy.save()
#
#         else:
#             payment.status = "failed"
#             payment.save()
#
#     except Payment.DoesNotExist:
#         pass
#
#     return HttpResponse("OK")


from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from .models import Payment
from vacancies.models import Vacancy, Category, Company

@csrf_exempt
def callback(request):
    payment_id = request.POST.get('payment_id')
    status = request.POST.get('status')

    try:
        payment = Payment.objects.get(payment_id=payment_id)
        if status == 'success':
            payment.status = 'success'
            payment.save()

            data = request.session.get('vacancy_data')
            if data:
                # Vakansiya yaradılır və aktiv edilir
                Vacancy.objects.create(
                    vacancy_name=data["vacancy_name"],
                    vacancy_description=data["vacancy_description"],
                    requirements=data["requirements"],
                    company_name_id=data["company_name"],
                    category_vacancy_id=data["category_vacancy"],
                    type_work_id=data["type_work"],
                    company_email=data["company_email"],
                    location_work=data["location_work"],
                    salary=data["salary"],
                    salary_type=data["salary_type"],
                    deadline=data["deadline"],
                )
        else:
            payment.status = 'failed'
            payment.save()
    except Payment.DoesNotExist:
        pass

    return redirect('payment:success' if status == 'success' else 'payment:cancel')
