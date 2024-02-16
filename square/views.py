from .models import *
from user.models import User
from .serializers import *
from .notification import send_notifications
from .filters import MealInfoFilter
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.viewsets import ModelViewSet
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import action


# class recruit_messageView(GenericAPIView):
#     queryset = recruit_message.objects.all()
#     serializer_class = recruit_messageSerializer


    # def get(self, request):
    #     serializer = self.get_serializer(instance=self.get_queryset(), many=True)
    #     return Response(serializer.data)
    #
    # def post(self, request):
    #     print("data", request.data)
    #     serializer = self.get_serializer(data=request.data)
    #     if serializer.is_valid():
    #         recruit_message.objects.create(**serializer.validated_data)
    #     else:
    #         return Response(serializer.errors)


# class meal_recordView(GenericAPIView):
#     queryset = recruit_message.objects.all()
#     serializer_class = meal_recordSerializer

    # def get(self, request):
    #     serializer = self.get_serializer(instance=self.get_queryset(), many=True)
    #     return Response(serializer.data)
    #
    # def post(self, request):
    #     print("data", request.data)
    #     serializer = self.get_serializer(data=request.data)
    #     if serializer.is_valid():
    #         recruit_message.objects.create(**serializer.validated_data)
    #     else:
    #         return Response(serializer.errors)


# class recruit_messageDetailView(GenericAPIView):
#     queryset = recruit_message.objects.all()
#     serializer_class = recruit_messageSerializers

    # def get(self, request, pk):
    #     serializer = self.get_serializer(instance=self.get_object(), many=False)
    #     return Response(serializer.data)
    #
    # def put(self, request, pk):
    #     print("data:", request.data)
    #     serializer = self.get_serializer(instance=self.get_object(), data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     else:
    #         return Response(serializer.errors)
    #
    # def delete(self, request, pk):
    #     self.get_object().delete()
    #     return Response()


# 操作单一约饭记录
# class meal_recordDetailView(GenericAPIView):
#     queryset = recruit_message.objects.all()
#     serializer_class = meal_recordSerializers

    # def get(self, request, pk):
    #     serializer = self.get_serializer(instance=self.get_object(), many=False)
    #     return Response(serializer.data)
    #
    # def put(self, request, pk):
    #     print("data:", request.data)
    #     serializer = self.get_serializer(instance=self.get_object(), data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     else:
    #         return Response(serializer.errors)
    #
    # def delete(self, request, pk):
    #     self.get_object().delete()
    #     return Response()


class recruit_messageView(ModelViewSet):
    queryset = MealInfo.objects.all()
    serializer_class = recruit_messageSerializer
    filter_backends = [DjangoFilterBackend]
    filter_class = MealInfoFilter
    ordering_fields = ['meal_time']
    def get_queryset(self):
        #前端传get
        grade = self.request.query_params.get('grade')
        queryset = MealInfo.objects.filter(grade__icontains=grade).filter(is_complete=False).order_by('meal_time')
        return queryset

    @action(methods=['put'], detail=True)
    def joined(self, request, *args, **kwargs):
        instance = self.get_object()
        if (instance.joined_num < (instance.member_num - 1)):
            participant_name = request.data.get('participant_name')
            participant = User.objects.get(username=participant_name)
            instance.participants.add(participant)
            instance.joined_num += 1
            instance.save()
            serializer = self.get_serializer(instance)
            send_notifications(request.user, '参加了约饭', instance.post_user)
            return Response(serializer.data)
        elif(instance.joined_num == (instance.member_num-1)):
            instance.is_complete = True
            return Response({'message':'已满员'})


class meal_recordView(ModelViewSet):
    queryset = MealInfo.objects.all()
    serializer_class = meal_recordSerializer

    def get_queryset(self):
        # 前端传get
        user_id = self.request.query_params.get('id')
        queryset = User.objects.filter(id=user_id).filter(is_complete=True).order_by('meal_time')
        return queryset


class LeftMessageView(ModelViewSet):
    queryset = LeftMessage.objects.all()
    serializer_class = LeftMessageSerializer

    def get_queryset(self):
        # 前端传get
        record_id = self.request.query_params.get('id')
        queryset = LeftMessage.objects.filter(meal__id=record_id)
        return queryset


#评价无需展示
class AppraiseView(ModelViewSet):
    queryset = Appraise.objects.all()
    serializer_class = AppraiseSerializer

    @action(methods=['post'], detail=False)
    def appraise(self, request):
        recipient = request.data.get('recipient')
        recipient.star = (recipient.star + request.data.get('star'))/2
        recipient.save()
        return Response({'message':'评价成功'})


class ShareView(ModelViewSet):
    queryset = Share.objects.all()
    serializer_class = ShareSerializer

    @action(methods=['put'], detail=True)
    def GetLike(self, request, pk):
        instance = self.get_object()
        instance.likes += 1
        instance.save()
        serializer = self.get_serializer(instance)
        send_notifications(request.user, '点赞了',instance.post_user)
        return Response(serializer.data)

'''
def user_notifications(request):
    unread_list = request.user.notifications.unread()
    #前端渲染？
'''