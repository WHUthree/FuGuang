from .models import *
from user.models import User
from .serializers import *
from .notification import send_notifications
from .filters import MealInfoFilter
from django_filters.rest_framework import DjangoFilterBackend
from .__init__ import overdue_scheduler
from datetime import datetime, timedelta
import pytz

from rest_framework.viewsets import ModelViewSet
from rest_framework import serializers,status
from rest_framework.response import Response
from rest_framework.decorators import action


class recruit_messageView(ModelViewSet):
    queryset = MealInfo.objects.filter(is_complete=False).order_by('meal_time')
    serializer_class = recruit_messageSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = MealInfoFilter

    def filter_queryset(self, queryset):
        queryset = super().filter_queryset(queryset)
        return queryset

    def perform_create(self, serializer):
        serializer.save(post_user=self.request.user)
        instance = serializer.save()
        instance.participants.add(self.request.user)
        overdue_scheduler.add_job(self.overdue, 'date', run_date=serializer.data['end_time'], args=[serializer.data['id']], id=str(serializer.data['id']))

    # 广场 招募信息
    @action(methods=['get'], detail=False, url_path='all')
    def all(self, request, *args, **kwargs):
        user = self.request.user
        grade = user.grade
        all_recruit_msg = self.filter_queryset(self.queryset).filter(is_full=False, is_overdue=False, grade__icontains=grade)
        serializer = self.get_serializer(all_recruit_msg, many=True)
        return Response(serializer.data)
    # 我的记录 进行中
    @action(methods=['get'], detail=False, url_path='ongoing')
    def my_ongoing(self, request, *args, **kwargs):
        ongoing_recruit_msg = self.get_queryset().filter(is_overdue=False, participants__in=[self.request.user])
        serializer = self.get_serializer(ongoing_recruit_msg, many=True)
        total_count = ongoing_recruit_msg.count()
        return Response({'total_count': total_count, 'results': serializer.data})
    # 我的记录 已过期
    @action(methods=['get'], detail=False, url_path='overdue')
    def my_overdue(self, request, *args, **kwargs):
        post_user = self.request.user
        overdue_recruit_msg = self.get_queryset().filter(is_overdue=True, post_user=post_user)
        serializer = self.get_serializer(overdue_recruit_msg, many=True)
        total_count = overdue_recruit_msg.count()
        return Response({'total_count': total_count, 'results': serializer.data})

    #有人应募
    @action(methods=['put'], detail=True, url_path='join')
    def join(self, request, *args, **kwargs):
        instance = self.get_object()
        if not instance.is_full:
            instance.participants.add(self.request.user)
            instance.joined_num += 1
            instance.save()
            if (instance.joined_num == (instance.member_num-1)):
                instance.is_full = True
                instance.save()
            serializer = self.get_serializer(instance)
            send_notifications(request.user, '参加了约饭', instance.post_user)
            return Response(serializer.data)
        else:
            return Response({'message':'已满员'})
    #有人取消应募
    @action(methods=['put'], detail=True, url_path='cancel')
    def cancel(self, request, *args, **kwargs):
        instance = self.get_object()
        cancel_user = request.user
        instance.participants.remove(cancel_user)
        instance.joined_num -= 1
        if (instance.is_full==True):
            instance.is_full = False
        instance.save()
        serializer = self.get_serializer(instance)
        if (instance.meal_time - datetime.now(tz=pytz.timezone('Asia/Shanghai')) <= timedelta(hours=4)):
            cancel_user.star = (cancel_user.star+2)/2
            cancel_user.save()
        send_notifications(cancel_user, '有人退出了约饭', instance.post_user)
        return Response(serializer.data)

    # 发布者删除招募
    @action(methods=['delete'], detail=True, url_path='delete')
    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        send_notifications(instance.post_user, '发布者取消了约饭', instance.participants.all())
        if (instance.meal_time - datetime.now(tz=pytz.timezone('Asia/Shanghai')) <= timedelta(hours=4)):
            post_user = instance.post_user
            post_user.star = (post_user.star+2)/2
            post_user.save()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    #过期处理
    def overdue(self,msg_id):
        instance = MealInfo.objects.filter(id=msg_id).first()
        if instance.is_full:
            instance.is_complete = True
            instance.save()
            overdue_scheduler.remove_job(msg_id)
        else:
            instance.is_overdue = True
            instance.save()
            overdue_scheduler.remove_job(msg_id)


class meal_recordView(ModelViewSet):
    queryset = MealInfo.objects.filter(is_complete=True).order_by('meal_time')
    serializer_class = meal_recordSerializer

    # 我的记录 待评价
    @action(methods=['get'], detail=False, url_path='completed')
    def my_completed(self, request, *args, **kwargs):
        participant = self.request.user
        completed_record = self.get_queryset().filter(participants__in=[participant]).exclude(appraise__giver=participant)
        serializer = self.get_serializer(completed_record, many=True)
        total_count = completed_record.count()
        return Response({'total_count': total_count, 'results': serializer.data})
    # 我的记录 已完成
    @action(methods=['get'], detail=False, url_path='appraised')
    def my_appraised(self, request, *args, **kwargs):
        participant = self.request.user
        appraised_record = self.get_queryset().filter(appraise__giver=participant, participants__in=[participant])
        serializer = self.get_serializer(appraised_record, many=True)
        total_count = appraised_record.count()
        return Response({'total_count': total_count, 'results': serializer.data})


class LeftMessageView(ModelViewSet):
    queryset = LeftMessage.objects.all()
    serializer_class = LeftMessageSerializer

    def get_queryset(self):
        record_id = self.request.query_params.get('id')
        queryset = LeftMessage.objects.filter(meal__id=record_id)
        return queryset

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)


# 评价无需展示
class AppraiseView(ModelViewSet):
    queryset = Appraise.objects.all()
    serializer_class = AppraiseSerializer

   #评价
    @action(methods=['post'], detail=False, url_path='give')
    def appraise(self, request, *args, **kwargs):
        recipient_id = request.data.get('recipient')
        recipient = User.objects.get(id=recipient_id)
        recipient.star = (recipient.star + int(request.data.get('star')))/2
        recipient.appraise_num += 1
        recipient.save()
        serializer = AppraiseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['recipient'] = recipient
            serializer.validated_data['meal'] = MealInfo.objects.get(id=request.data.get('meal'))
            serializer.save(giver=self.request.user)
        else:
            return Response(serializer.errors)
        return Response({'message':'评价成功'})


class ShareView(ModelViewSet):
    queryset = Share.objects.all().order_by('-post_time')
    serializer_class = ShareSerializer

    def perform_create(self, serializer):
        serializer.save(post_user=self.request.user)

    # 广场 分享
    @action(methods=['get'], detail=False, url_path='all')
    def all(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)
    # 我的 分享
    @action(methods=['get'], detail=False, url_path='mine')
    def mine(self, request, *args, **kwargs):
        post_user = self.request.user
        my_share = self.get_queryset().filter(post_user=post_user)
        serializer = self.get_serializer(my_share, many=True)
        total_count = my_share.count()
        return Response({'total_count': total_count, 'results': serializer.data})
    # 我的 赞过
    @action(methods=['get'], detail=False, url_path='liked')
    def my_liked(self, request, *args, **kwargs):
        liker = self.request.user
        my_liked = self.get_queryset().filter(liked_by__in=[liker])
        serializer = self.get_serializer(my_liked, many=True)
        total_count = my_liked.count()
        return Response({'total_count': total_count, 'results': serializer.data})

    # 点赞
    @action(methods=['put'], detail=True, url_path='like')
    def Like(self, request, pk):
        instance = self.get_object()
        instance.likes += 1
        instance.liked_by.add(self.request.user)
        instance.save()
        serializer = self.get_serializer(instance)
        send_notifications(request.user, '点赞了',instance.post_user)
        return Response(serializer.data)
    # 取消赞
    @action(methods=['put'], detail=True, url_path='cancellike')
    def CancelLike(self, request, pk):
        instance = self.get_object()
        instance.likes -= 1
        instance.liked_by.remove(self.request.user)
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

'''
def user_notifications(request):
    unread_list = request.user.notifications.unread()
    #前端渲染？
'''