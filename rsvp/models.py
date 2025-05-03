'''
INF601 - Advanced Programming in Python
Assignment: Final Project
I,     Levi Eck    , affirm that the work submitted for this assignment is entirely my own. I have not engaged in any form of academic dishonesty, including but not limited to cheating, plagiarism, or the use of unauthorized materials. I have neither provided nor received unauthorized assistance and have accurately cited all sources in adherence to academic standards. I understand that failing to comply with this integrity statement may result in consequences, including disciplinary actions as determined by my course instructor and outlined in institutional policies. By signing this statement, I acknowledge my commitment to upholding the principles of academic integrity.
'''

### INF601 - Advanced Programming in Python
### Levi Eck
### Final Project

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
    event = models.ForeignKey('Event', on_delete=models.CASCADE, related_name='guests', null=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    #is_invited = models.BooleanField(default=True)
    has_rsvped = models.BooleanField(default=False)
    #attending = models.BooleanField(null=True, blank=True)  # Yes/No/Undecided
    #message = models.TextField(blank=True)

    def __str__(self):
        return self.name

