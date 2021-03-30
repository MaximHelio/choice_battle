from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Choice, Movie
from django.urls import reverse


# Create your views here.
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies,
    }
    return render(request, 'movies/index.html', context)

def vote(request, question_id):
    question = get_object_or_404(Movie, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def results(request, question_id):
    question = get_object_or_404(Movie, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
