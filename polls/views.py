from django.shortcuts import render, HttpResponse, HttpResponseRedirect 
from .models import Question
from django.shortcuts import get_object_or_404
from django.urls import reverse

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'questions': latest_question_list}
    return render(request, 'polls/index.html', context=context)


def detail(request,question_id):
    questions = get_object_or_404(Question,pk=question_id)
    context = {'questions': questions}
    return render(request, 'polls/detail.html', context=context)

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'polls/results.html', context)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html'), {
            'question': question,
            'error_message': "You didn't select a choice",
        }
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

    
        
    return HttpResponse(f'You are looking at the results of {question_id}')