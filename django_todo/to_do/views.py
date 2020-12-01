from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import NewTask
from .forms import TaskForm
from django.contrib import messages
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


# @login_required(login_url = "login")
# def home(request):
#     tasks = NewTask.objects.all().filter(user=request.user)
#     user_id = User.objects.get(id = request.user.id)

#     content = {'tasks': tasks, 'user_id':user_id}
#     return render(request, "to_do/home.html", content)

class HomeView(LoginRequiredMixin, ListView):
    model = NewTask

    def get_query(self):
        queryset = NewTask.objects.all().filter(user=self.request.user)
        return queryset


    paginate_by = 3
    template_name = "to_do/home.html"




@login_required()
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

    return render(request, "to_do/new_task.html", content)


# def task_view(request, pk):
#     task = NewTask.objects.get(id=pk)
#     content = {'task': task}
#     return render(request, "to_do/task_view.html", content)


class TaskDatatilView(LoginRequiredMixin, DetailView):
    model = NewTask
    template_name = "to_do/task_view.html"






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
    return render(request, "to_do/task_update.html", content)


def task_delete(request, pk):
    task = NewTask.objects.get(id=pk)
    task.delete()
    messages.add_message(request, messages.SUCCESS, "User deleted the task.")
    return redirect("home")