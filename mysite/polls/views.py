from django.http import Http404
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
# 1-2. from django.template import loader

from .models import Question


def index(request):
    # 3.
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context)
    # 2.
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('polls/index.html')
    # context = {
    #     'latest_question_list': latest_question_list,
    # }
    # return HttpResponse(template.render(context, request))

    # 1.
    # output = ', '.join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)


def detail(request, question_id):
    # 1.
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exits")
    # 2.
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    response = "You're looking at the results of question {}."
    return HttpResponse(response.format(question_id))


def vote(request, question_id):
    return HttpResponse("You're voting on question {}.".format(question_id))
