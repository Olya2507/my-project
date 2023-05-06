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

    """При запросе GET возвращаем contact_form.html представление, а так же заголовок."""

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
        return render(request, 'contact_form.html', context={'form': form,
                                                             })


    """При запросе POST мы забираем все что было отправленно через форму. Отправку письма мы оборачиваем в конструкцию try/except.
В send_mail мы помещаем такие поля как subject, message, from_email и почту куда мы отправляем письмо
 (на скрине из документации эти поля описаны.) Не можем сюда ничего лишнего поместить, только аргументы, которые 
 предполагает функция. Если возникнет ошибка BadHeaderError, мы вернем сообщение "Невалидный заголовок".после успешной отправки мы
  редиректим пользователя на страницу success."""


class SuccessView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'success.html', context={
            'title': 'Спасибо'
        })


    """рендерим наше представление и передаем заголовок """