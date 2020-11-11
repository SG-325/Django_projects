from django.shortcuts import render
from django.contrib.auth import authenticate
import json

# Create your views here.
def home(request):
	return render(request, "home_app/h.html")




def task_1(request):
	with open("sample_json.json","r") as f:
		value_json = json.load(f)

	return render(request, "home_app/h_1.html", value_json)




def task_2(request):
	return render(request, "home_app/h_2.html")




def task_3(request):
	d1 = {'a': 100, 'b': 200, 'c':300}
	d2 = {'a': 300, 'b': 200, 'd':400}

	for i in d1:
		if i in d2:
			d2.update({i:(d1[i]+d2[i])})
		else:
			d2.update({i:d1[i]})

	content = {"name":d2}
	return render(request, "home_app/h_3.html", content)