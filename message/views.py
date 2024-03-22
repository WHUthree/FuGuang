from django.shortcuts import redirect
from django.urls import reverse
from django.http import JsonResponse
from django.core.serializers import serialize

from user.models import User
from .models import Message

# 系统消息推送
def unread(request,uid):
    user = User.objects.get(id=uid)
    unread_list = user.notifications.unread()
    data = serialize('json',unread_list)
    return JsonResponse(data,safe=False)

def read(request,uid):
    user = User.objects.get(id=uid)
    read_list = user.notifications.read()
    data = serialize('json',read_list)
    return JsonResponse(data,safe=False)

def change_status(request,uid):
    user = User.objects.get(id=uid)
    user.notifications.mark_all_as_read()
    return redirect(reverse('read',kwargs={'uid':uid}))


# 聊天室
def show(request, gid):
    queryset = Message.objects.filter(group=gid).order_by('send_time')
    serialized_data = serialize('json',queryset)
    data = {
        'msgs': serialized_data,
        'group_id':gid
    }
    return JsonResponse(data,safe=False)

def send(request, gid, uid):
    message = request.POST.get('txt')
    sender = User.objects.get(id=uid)
    Message.objects.create(group=gid, sender=sender, content=message)
    return redirect(reverse('show', kwargs={'gid': gid}))
