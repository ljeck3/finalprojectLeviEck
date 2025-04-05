from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the rsvp index.")

def detail(request, guest_id):
    return HttpResponse("You're looking at guest %s." % guest_id)