from .forms import UserRegistrationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
    




def register(request):

    if request.method != 'POST':

        form = UserRegistrationForm()
    else:
   
        form = UserRegistrationForm(data=request.POST)
        
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'registration/register.html', context)
