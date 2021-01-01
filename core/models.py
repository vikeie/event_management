from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=50)
    venue = models.CharField(max_length=200)
    date = models.DateTimeField(help_text='Please use the following format: <em>YYYY-MM-DD HH:MM:SS</em>.')
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    attendees = models.ManyToManyField(User, related_name='attending', blank=True)
    num_of_attendees = models.PositiveIntegerField(default=0, blank=True)

    class Meta:
        ordering = ['date']

    def __str__(self):
        return self.name
