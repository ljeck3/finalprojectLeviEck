from django.db import models


class Guest(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    is_invited = models.BooleanField(default=True)
    has_rsvped = models.BooleanField(default=False)
    attending = models.BooleanField(null=True, blank=True)  # Yes/No/Undecided
    message = models.TextField(blank=True)

    def __str__(self):
        return self.name

