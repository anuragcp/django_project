from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm  # this form is used for user creation
from django.contrib import messages
from .forms import UserRegisterForm

def register(request):

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save() # saves data to the user
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('blog-home')
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', context={'form':form})
    
