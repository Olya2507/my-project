from .forms import FeedBackForm
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views import View

class FeedBackView(View):
    def get(self, request, *args, **kwargs):
        form = FeedBackForm()
        return render(request, 'contact_form.html', context={
            'form': form,
            'title': 'Написать мне'
        })

    def post(self, request, *args, **kwargs):
        form = FeedBackForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            from_email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            try:
                send_mail(f'От {name, from_email} | {subject}', message, from_email, ['olyshka250783@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Невалидный заголовок')
            return HttpResponseRedirect('success')
        return render(request, 'contact_form.html', context={
            'form': form,
        })

class SuccessView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'success.html', context={
            'title': 'Спасибо'
        })