from django.contrib.messages import success
from django.shortcuts import render
from contact.forms import ContactForm


def contact(request):
    success = False
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            success = True
            form = ContactForm()

    context = {
        'form': form,
        'success': success
    }
    return render(request, 'contact/contact.html',context)
