from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import NewUserForm
from django.contrib import messages


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('task_list')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    else:
        if request.user.is_authenticated:
            return redirect('task_list')
        return render(request, 'login.html')


def register_view(request):
    form = NewUserForm()
    context = {}

    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            context['success_message'] = "Registration successful."

    else:
        if request.user.is_authenticated:
            return redirect('task_list')

    context["register_form"] = form
    return render(request=request, template_name="register.html", context=context)


def logout_view(request):
    logout(request)
    return redirect('login')