from django.db import models
import datetime
from django.utils import timezone
from django.contrib import admin



class Event(models.Model):
    event_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Guest(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    is_invited = models.BooleanField(default=True)
    has_rsvped = models.BooleanField(default=False)
    attending = models.BooleanField(null=True, blank=True)  # Yes/No/Undecided
    message = models.TextField(blank=True)

    def __str__(self):
        return self.name

