from django.shortcuts import render, redirect
from django.urls import reverse

from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from .models import Message
from .serializers import MessageSerializer

# Create your views here.
# 前端需要重写,json传数据,用序列化器

def show(request,gid):
    if(request.method == 'GET'):
        queryset = Message.objects.filter(group=gid).order_by('send_time')
        return render(request,"show.html",{'group_id':gid,'msgs':queryset})
    else:
        message = request.POST.get('txt')
        Message.objects.create(group=gid,content=message)
        return redirect(reverse('show',kwargs={'gid':gid}))

'''
class MessageView(GenericAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def get(self,request,group_id):
        filtered_queryset = self.get_queryset().filter(group=group_id).order_by('send_time')
        serialized_data = self.get_serializer(instance=filtered_queryset, many=True)
        return Response(serialized_data.data)

    def post(self,request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            Message.objects.create(**serializer.validated_data)
        else:
            return Response(serializer.errors)
'''