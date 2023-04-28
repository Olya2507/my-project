from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse



def contacts(request):
    return render(request, 'contact.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Пробное сообщение"
            body = {
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
                'email': form.cleaned_data['email_address'],
                'phone': form.cleaned_data['phone'],
                'message': form.cleaned_data['message'],
            }
            message = "\n".join(body.values())
            try:
                send_mail(subject, message,
                          'admin@example.com',
                          ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Найден некорректный заголовок')
            return redirect("contact:contact9")

    form = ContactForm()
    return render(request, "contact9.html", {'form': form})

