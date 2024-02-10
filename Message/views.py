from django.shortcuts import render

# Create your views here.

def show(request):
    group_id = request.GET.get('gid')
    return render(request,"show.html",{'group_id':group_id})