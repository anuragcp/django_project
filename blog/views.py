from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Post
from django.views.generic import ListView

# dummy data
# posts = [
#     {
#         'author':'Anurag',
#         'title': 'Blog Post 1',
#         'content': 'First post content',
#         'date_posted': 'August 27 2018'
#     },
#     {
#         'author':'Shyamrag',
#         'title': 'Blog Post 2',
#         'content': 'Second things',
#         'date_posted': 'August 28 2018'
#     }
# ]


def home(request):
    context = {
        'posts' : Post.objects.all()
    }
    return render(request, 'blog/home.html', context=context)

def about(request):
    return render(request, 'blog/about.html', context={'title': 'About'})

# class based view looks for templates with certain naming patterns
# <app>/<model>_<viewtype>.html - is is also possible to change the template

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'    # by default <app>/<model>_<viewtype>.html - is is also possible to change the template
    context_object_name = 'posts'
    ordering = ['data_posted']

