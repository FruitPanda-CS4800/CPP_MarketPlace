from django.shortcuts import render
from Messaging.models import Thread
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def messages_page(request):
    threads = Thread.objects.by_user(user=request.user).prefetch_related('chatmessage_thread').order_by('timestamp')
    context = {
        'Threads': threads
    }
    return render(request, 'messaging.html')