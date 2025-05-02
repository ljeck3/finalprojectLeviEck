'''
INF601 - Advanced Programming in Python
Assignment: Mini Project 4
I,     Levi Eck    , affirm that the work submitted for this assignment is entirely my own. I have not engaged in any form of academic dishonesty, including but not limited to cheating, plagiarism, or the use of unauthorized materials. I have neither provided nor received unauthorized assistance and have accurately cited all sources in adherence to academic standards. I understand that failing to comply with this integrity statement may result in consequences, including disciplinary actions as determined by my course instructor and outlined in institutional policies. By signing this statement, I acknowledge my commitment to upholding the principles of academic integrity.
'''

### INF601 - Advanced Programming in Python
### Levi Eck
### Final Project

from django.db import models
import datetime
from django.utils import timezone
from django.contrib import admin


class Gift(models.Model):
    gift_item = models.CharField(max_length=200)
    has_been_claimed = models.BooleanField(default=False)