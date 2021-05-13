from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from .models import Question, Choice
from django.template import loader
from django.urls import reverse
from django.views import generic

# Create your views here.


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return last five published questions"""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    # #output = ', '.join([q.quation_text for q in latest_question_list])
    # return HttpResponse(template.render(context, request))
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    #return HttpResponse("You're looking at question %s" % question_id)
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except:
    #     raise Http404("Question doesn't exist")
    # return render(request, 'polls/detail.html', {'question': question})
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question':question})


# def results(request, question_id):
#     response = "You're looking at the results of question %s"
#     return HttpResponse(response % question_id)

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question':question})


# def vote(request, question_id):
#     return HttpResponse("You are voting on question %s" % question_id)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        ind = request.POST['choice']
        print(ind)
        if ind == '-1':
            print("qwe")
            text = request.POST['comment101']
            print(text)
            question.choice_set.create(choice_text=text, votes=0)
            ind = question.choice_set.filter(choice_text__startswith=text)[0].id
        print(ind)
        selected_choice = question.choice_set.get(pk=ind)
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice"
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question_id, )))