from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone


from .models import Memo

def index(request):
    latest_memo_list = Memo.objects.order_by("-pub_date")[:5]
    context = {"latest_memo_list": latest_memo_list}
    return render(request, "guestbook/index.html", context)

def detail(request, memo_id):
    memo = get_object_or_404(Memo, pk=memo_id)
    return render(request, "guestbook/detail.html", {"memo": memo})


#TRY TO REWRITE THIS FOR MESSAGE

def compose(request):
    if request.method == 'POST':
        name = request.POST['name']
        content = request.POST['content']

        memo = Memo.objects.create(name=name, content=content, pub_date=timezone.now())

        memo.save()
        return render(request, 'guestbook/compose.html')
    else:
        return render(request, 'guestbook/compose.html')
        #message = "Thank you for RSVPing!"
        #return render(request, "guestbook/results.html", {"message": message})