from django.db import models

# Create your models here.

STATUS_CHOICES = (
					(0, "New"),
					(1, "Doing"),
					(2, "Done"),
					)

class NewTask(models.Model):
	name = models.CharField(max_length=30)
	description = models.TextField()
	date = models.DateTimeField(auto_now_add = True)
	status = models.IntegerField(choices = STATUS_CHOICES)

	def __str__(self):
		return self.name