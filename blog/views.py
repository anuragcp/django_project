from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView, 
    UpdateView,
    DeleteView)

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
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post
    

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

    # since we are provide the primary key details,
    # even the post_form template will taken as the login template
