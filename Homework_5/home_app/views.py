from django.shortcuts import render, redirect
from .models import NewTask
from .forms import TaskForm
from django.http import HttpResponseRedirect


# Create your views here.

def home(request):
	tasks = NewTask.objects.all()
	content = {"tasks":tasks}
	return render(request, "home_app/home.html", content)




def create_task(request):
	tasks = NewTask.objects.all()

	if request.method == "POST":
		form = TaskForm(request.POST)

		if form.is_valid():
			form.save()

		return redirect("home")

	form = TaskForm()
	content = {"form":form}
	return render(request, "home_app/new_task.html", content)




def update_task(request, pk):
	tasks = NewTask.objects.all().filter(id = pk)[0]

	if request.method == "POST":
		form = TaskForm(request.POST, instance = tasks)
		if form.is_valid():
			form.save()
		return redirect("home")


	form = TaskForm(instance = tasks)
	content = {"form":form}
	return render(request, "home_app/new_task.html", content)




def view_task(request, pk):
	tasks = NewTask.objects.all().filter(id = pk)[0]

	form = TaskForm(instance = tasks)
	content = {
				"form":form,
				"id":pk
				}
	return render(request, "home_app/task_view.html", content)





def delete_task(request, pk):

	if request.method == "POST":
		tasks = NewTask.objects.all().get(id = pk).delete()
		return HttpResponseRedirect("/")

	return render(request, 'home_app/task_delete.html')

