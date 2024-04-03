from django.shortcuts import render
from movie.models import Movie
from movie.forms import Add

def home(request):

    m=Movie.objects.all()
    return render(request,'home.html',{'m':m})

def addmovie(request):

    if(request.method=="POST"):
        f=Add(request.POST,request.FILES)
        if f.is_valid():
            f.save()
            return home(request)

    f=Add()
    return render(request,'addmovie.html',{'f':f})

def details(request,n):

    d=Movie.objects.get(id=n)
    return render(request,'details.html',{'d':d})

def Movieupdate(request,n):
    ed=Movie.objects.get(id=n)
    if(request.method=="POST"):
        f=Add(request.POST,request.FILES,instance=ed)
        if f.is_valid():
            f.save()
            return home(request)


    f=Add(instance=ed)
    return render(request,'addmovie.html',{'f':f})

def Moviedelete(request,n):
    dlt=Movie.objects.get(id=n)
    dlt.delete()

    return home(request)

