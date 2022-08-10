from django.http import HttpResponse
from django.shortcuts import render

from .models import place
from .models import guide
# Create your views here.
# def demo(request):
#     return render(request,"index.html")
#     # return HttpResponse("hello world")
#
# def aboutme(request):
#     return render(request,"aboutme.html")
#
# def contact(request):
#     return HttpResponse("student at inmakes")



# def demo(request):
#     name="India"
#     return render(request,"index.html",{"obj":name})
# def addition(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     total=x+y
#     return render(request,"result.html",{'result':total})


def demo(request):
    obj = place.objects.all()
    obj1 = guide.objects.all()
    return render(request, "index.html", {'result': obj,'result1': obj1})

