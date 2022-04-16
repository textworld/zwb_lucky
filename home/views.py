
from django.http import HttpResponse
from .tasks import make_lucky
import uuid
from django.http import JsonResponse
from .models import Ticket
from django.shortcuts import render


def get_make_lucky(request):
    identity = uuid.uuid4()
    make_lucky.delay(identity)
    return JsonResponse({'status': 0, 'message': '创建成功', 'data': identity})


def index_view(request):
    tickets = Ticket.objects.all()
    context = {
        "tickets": tickets
    }
    return render(request, "index.html", context)
