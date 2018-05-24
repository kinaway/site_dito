from django.db import models

class Event(models.Model):
	user_id = models.ForeignKey(
		'auth.User',
		on_delete=models.CASCADE)
	event_description = models.CharField(max_length=200)
	date = models.DateTimeField()

	def __str__(self):
		return self.event_description