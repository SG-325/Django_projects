from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.


def task_1(request):
	text = "Hello!!! If you want to get some information go to task_2/"
	return HttpResponse(text)
		


def task_2(request):
	text = "In task_3/ you can find out the date today. In task_4/ you can see the result of the program.In task_5/ you can see even numbers and odd numbers"
	return HttpResponse(text)


def task_3(request):
	time = datetime.now()
	date = f"Today is {time.day}/{time.month}/{time.year}. The time now is {time.hour}:{time.minute}:{time.second}"

	return HttpResponse(date)


def task_4(request):
	dict_ = {}
	
	for i in range(1,16):
		dict_.update({i:i**2})
	
	text = "The result of the program:" + str(dict_)

	return HttpResponse(text)


def task_5(request):
	odd_list = []
	even_list = []
	for i in range(1,16):
		if i % 2 == 0:
			even_list.append(i)
		else:
			odd_list.append(i)

	text = f"Odd numbers: {str(odd_list)}\n Even numbers: {str(even_list)}"
	return HttpResponse(text)

