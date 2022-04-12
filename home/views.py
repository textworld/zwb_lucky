
from django.http import HttpResponse
from .tasks import send_email_with_pic
from .tasks import make_lucky
import uuid
from django.http import JsonResponse


def get_make_lucky(request):
    identity = uuid.uuid4()
    make_lucky.delay(identity)
    return JsonResponse({'status': 0, 'message': '创建成功', 'data': identity})
