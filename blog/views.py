from django.shortcuts import render
from django.http import HttpResponse

# dummy data
posts = [
    {
        'author':'Anurag',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27 2018'
    },
    {
        'author':'Shyamrag',
        'title': 'Blog Post 2',
        'content': 'Second things',
        'date_posted': 'August 28 2018'
    }
]


def home(request):
    context = {
        'posts' : posts
    }
    return render(request, 'blog/home.html', context=context)

def about(request):
    return render(request, 'blog/about.html', context={'title': 'About'})
