from .models import recruit_message
from .models import meal_record
from rest_framework.generics import GenericAPIView
from rest_framework import serializers
from rest_framework.response import Response


class recruit_messageSerializers(serializers.ModelSerializer):
    class Meta:
        model = recruit_message
        fields = "__all__"
class meal_recordSerializers(serializers.ModelSerializer):
    class Meta:
        model = meal_record
        fields = "__all__"
class recruit_messageView(GenericAPIView):
    queryset = recruit_message.objects.all()
    serializer_class = recruit_messageSerializers
    def get(self,request):
        serializer = self.get_serializer(instance=self.get_queryset(), many=True)
        return Response(serializer.data)
    def post(self,request):
        print("data",request.data)
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            recruit_message.objects.create(**serializer.validated_data)
        else:
            return Response(serializer.errors)
class meal_recordView(GenericAPIView):
    queryset = meal_record.objects.all()
    serializer_class = meal_recordSerializers
    def get(self,request):
        serializer = self.get_serializer(instance=self.get_queryset(), many=True)
        return Response(serializer.data)
    def post(self,request):
        print("data",request.data)
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            meal_record.objects.create(**serializer.validated_data)
        else:
            return Response(serializer.errors)
class recruit_messageDetailView(GenericAPIView):
    queryset = recruit_message.objects.all()
    serializer_class = recruit_messageSerializers
    def get(self,request,pk):
        serializer = self.get_serializer(instance=self.get_object(), many=False)
        return Response(serializer.data)
    def put(self,request,pk):
        print("data:", request.data)
        serializer = self.get_serializer(instance=self.get_object(),data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    def delete(self,request,pk):
        self.get_object().delete()
        return Response()
#操作单一约饭记录
class meal_recordDetailView(GenericAPIView):
    queryset = meal_record.objects.all()
    serializer_class = meal_recordSerializers
    def get(self,request,pk):
        serializer = self.get_serializer(instance=self.get_object(), many=False)
        return Response(serializer.data)
    def put(self,request,pk):
        print("data:", request.data)
        serializer = self.get_serializer(instance=self.get_object(),data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    def delete(self,request,pk):
        self.get_object().delete()
        return Response()