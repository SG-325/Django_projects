from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import NewTask
from .forms import TaskForm
from django.contrib import messages

# Create your views here.

@login_required(login_url = "login")
def home(request):
    tasks = NewTask.objects.all().filter(user=request.user)
    user_id = User.objects.get(id = request.user.id)

    content = {'tasks': tasks, 'user_id':user_id}
    return render(request, "home_app/home.html", content)


@login_required(login_url = "login")
def new_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit = False)
            task.user = User.objects.get(id = request.user.id)
            task.save()
            messages.add_message(request, messages.SUCCESS, "User created a new task.")

        return redirect('home')

    form = TaskForm()
    content = {'form': form}

    return render(request, "home_app/new_task.html", content)


def task_view(request, pk):
    task = NewTask.objects.get(id=pk)
    content = {'task': task}
    return render(request, "home_app/task_view.html", content)


def task_update(request, pk):
    task = NewTask.objects.get(id=pk)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "User updated the task.")

        return redirect('home')

    form = TaskForm(instance=task)
    content = {'form': form}
    return render(request, "home_app/task_update.html", content)


def task_delete(request, pk):
    task = NewTask.objects.get(id=pk)
    task.delete()
    messages.add_message(request, messages.SUCCESS, "User deleted the task.")
    return redirect("home")
