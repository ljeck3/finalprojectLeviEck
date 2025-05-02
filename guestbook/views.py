'''
INF601 - Advanced Programming in Python
Assignment: Final Project
I,     Levi Eck    , affirm that the work submitted for this assignment is entirely my own. I have not engaged in any form of academic dishonesty, including but not limited to cheating, plagiarism, or the use of unauthorized materials. I have neither provided nor received unauthorized assistance and have accurately cited all sources in adherence to academic standards. I understand that failing to comply with this integrity statement may result in consequences, including disciplinary actions as determined by my course instructor and outlined in institutional policies. By signing this statement, I acknowledge my commitment to upholding the principles of academic integrity.
'''

### INF601 - Advanced Programming in Python
### Levi Eck
### Final Project


from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from .models import Memo

@login_required(login_url="/members/login_user/")
def index(request):
    latest_memo_list = Memo.objects.order_by("-pub_date")[:5]
    context = {"latest_memo_list": latest_memo_list}
    return render(request, "guestbook/index.html", context)

def detail(request, memo_id):
    memo = get_object_or_404(Memo, pk=memo_id)
    return render(request, "guestbook/detail.html", {"memo": memo})



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