from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import order
from .form import Todoform
# Create your views here.
def home(request):
    tb = order.objects.all()
    context = {
        'tb':tb,
    }
    return render(request,'ajax/home.html',context)

def detail(request,id):
    tb = order.objects.get(id=id)
    context = {
        'tb':tb,
    }
    return render(request,'ajax/detail.html',context)

def add(request):
    form1 = Todoform(request.POST or None)
    if form1.is_valid():
        form1.save()
        return redirect('/')
    context = {
        'form':form1,
    }
    return render(request,'ajax/add.html',context)

def update(request,id):
    tb = order.objects.get(id=id)
    form1 = Todoform(request.POST or None , instance=tb)

    if form1.is_valid():
        form1.save()
        return redirect('/')
    context = {
        'form':form1,
    }
    return render(request,'ajax/update.html',context)


def delete(request,id):
    data = order.objects.get(id=id)
    data.delete()
    return redirect('/')