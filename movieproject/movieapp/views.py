from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Movie
from . forms import mform
# Create your views here.

def index(request):
    movie= Movie.objects.all()
    return render(request,"index.html", {'movie':movie})

def fun(request,mid):
    # return HttpResponse("This is %s" % mid)
    movie=Movie.objects.get(id=mid)
    return render(request,"detail.html",{'movie':movie})

def addmovie(request):
    if request.method=="POST":
        name = request.POST.get('name',)
        txt = request.POST.get('txt', )
        year = request.POST.get('year', )
        img = request.FILES['img']
        movie = Movie(name=name,txt=txt,year=year,img=img)
        movie.save()

    return render(request,'add.html')

def update(request,id):
    movie = Movie.objects.get(id=id)
    form=mform(request.POST or None, request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'movie':movie})

def delete(request, id):
    if request.method=="POST":
        movie = Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')