from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    mobile_number = models.CharField(max_length=15, blank=True, null=True)
    full_name = models.CharField(max_length=15)
    # USERNAME_FIELD = 'email'

    def __str__(self):
        return self.username

class Event(models.Model):
    title = models.CharField(max_length=50)
    venue = models.CharField(max_length=200)
    date = models.DateTimeField(help_text='Please use the following format: <em>YYYY-MM-DD HH:MM:SS</em>.')
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    num_of_attendees = models.PositiveIntegerField(default=0, blank=True)

    class Meta:
        ordering = ['date']

    def __str__(self):
        return self.name
