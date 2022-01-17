from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Question
from django.template import loader
from django.http import Http404

def index(request, render_method_num=0):
    match render_method_num:

        case 0:
            # The full way to load a template
            # This makes it eaiser to read/translate what the render sequence is actually doing.
            latest_question_list = Question.objects.order_by('-pub_date')[:5]
            template = loader.get_template('polls/index.html')
            context = {
                'latest_question_list' : latest_question_list,
            }
            return HttpResponse(template.render(context, request))

        case 1:
            return _load_index_(request)

        case 2:
            # The shortcut for loading a template
            # The template assignment isn't needed. Just use the render method, the request, the path, and the context.
            latest_question_list = Question.objects.order_by('-pub_date')[:5]
            context = {
                'latest_question_list' : latest_question_list,
            }
            return render(request, 'polls/index.html', context)

        case _:
            raise Http404('That page has not been made yet.')       

def detail(request, question_id):
    match question_id:

        case 0:
            try:
                question = Question.objects.get(pk=question_id)
            except:
                raise Http404('That question hasn\'t been asked yet.')
            return HttpResponse('You\'re looking at question %s.' % question_id)
        
        case _:
            question = get_object_or_404(Question, pk=question_id)
            template = loader.get_template('polls/detail.html')
            context = {
                'route_message' : 'The default case ran.',
                'question' : question
            }
            return HttpResponse(template.render(context, request))

def results(request, question_id):
    response = 'You\'re looking at question %s.'
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse('You\'re voting on question %s.' % question_id)

def _load_index_(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list' : latest_question_list,
    }
    return HttpResponse(template.render(context, request))