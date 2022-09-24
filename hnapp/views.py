from django.shortcuts import render
from .models import Stories, JobStories, AskStories
from django.core.paginator import Paginator



"""
List all items in database and add pagination
"""
def index_view(request):
    
    story = Stories.objects.all().order_by('-date_created')
    paginator = Paginator(story, 10)
    page_number = request.GET.get('page')
    place_list = paginator.get_page(page_number)
    context = {
        'Title':'Hacker News',
        'paginator': place_list
    }
    return render(request, 'hnapp/index.html', context)

"""
filter from database for show category
"""
def show_category(request):
    
    story = Stories.objects.filter(title__contains="Show HN").order_by('-date_created')
    paginator = Paginator(story, 10)
    page_number = request.GET.get('page')
    place_list = paginator.get_page(page_number)
    context = {
        'Title': 'Show | Hacker News',
        'paginator': place_list
    }
    return render(request, 'hnapp/show.html', context)

"""
filter from database for job stories
"""
def job_category(request):
    
    story = JobStories.objects.all().order_by('-date_created')
    paginator = Paginator(story, 10)
    page_number = request.GET.get('page')
    place_list = paginator.get_page(page_number)
    context = {
        'Title': 'Jobs | Hacker News',
        'paginator': place_list
    }
    return render(request, 'hnapp/jobs.html', context)

"""
filter from database for ask stories
"""
def ask_category(request):
    
    story = AskStories.objects.all().order_by('-date_created')
    paginator = Paginator(story, 10)
    page_number = request.GET.get('page')
    place_list = paginator.get_page(page_number)
    context = {
        'Title': 'Ask | Hacker News',
        'paginator': place_list
    }
    return render(request, 'hnapp/ask.html', context)

"""
filter from database for ask story details
"""
def ask_details(request, id):
    
    story = AskStories.objects.get(id=id)
    context = {
        'Title': 'Ask | Hacker News',
        'story': story
    }
    return render(request, 'hnapp/ask-details.html', context)

