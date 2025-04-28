from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse


from .models import Message

def index(request):
    latest_message_list = Message.objects.order_by("-pub_date")[:5]
    context = {"latest_message_list": latest_message_list}
    return render(request, "guestbook/index.html", context)

def detail(request, message_id):
    message = get_object_or_404(Message, pk=message_id)
    return render(request, "guestbook/detail.html", {"message": message})