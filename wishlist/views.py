'''
INF601 - Advanced Programming in Python
Assignment: Final Project
I,     Levi Eck    , affirm that the work submitted for this assignment is entirely my own. I have not engaged in any form of academic dishonesty, including but not limited to cheating, plagiarism, or the use of unauthorized materials. I have neither provided nor received unauthorized assistance and have accurately cited all sources in adherence to academic standards. I understand that failing to comply with this integrity statement may result in consequences, including disciplinary actions as determined by my course instructor and outlined in institutional policies. By signing this statement, I acknowledge my commitment to upholding the principles of academic integrity.
'''

### INF601 - Advanced Programming in Python
### Levi Eck
### Final Project

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect



from .models import Gift

@login_required(login_url="/members/login_user/")
def index(request):
    gift_item_list = Gift.objects.all()#.order_by("-gift_item")[:5]
    context = {"gift_item_list": gift_item_list}
    return render(request, "wishlist/index.html", context)

def detail(request, gift_id):
    gift = get_object_or_404(Gift, pk=gift_id)
    return render(request, "wishlist/detail.html", {"gift": gift})

def respond(request, gift_id):
    if request.method == 'POST':
        claim = 'claim' in request.POST

        gift = get_object_or_404(Gift, id=gift_id)
        gift.has_been_claimed = claim
        gift.save()

        return redirect('wishlist:index')
    else:
        return redirect('wishlist:index')

def results(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    return render(request, "rsvp/results.html", {"event": event})
