from django.contrib import admin

from .models import Event
from .models import Guest


admin.site.register(Event)
admin.site.register(Guest)

