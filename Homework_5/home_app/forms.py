from django.forms import ModelForm
from django import forms
from .models import NewTask


class TaskForm(ModelForm):
	class Meta:
		model = NewTask
		fields = '__all__'




