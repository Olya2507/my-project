from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import Choice, Question

class IndexView(generic.ListView):
    template_name = 'app_index.html'
    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:3]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'app_detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'app_results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'app_detail.html', {
            'question': question,
            'error_message': "Вы не выбрали ответ.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('results', args=(question.id,)))