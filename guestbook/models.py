from django.db import models
import datetime
from django.utils import timezone
from django.contrib import admin

class Memo(models.Model):
    name = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField("date published")

    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

