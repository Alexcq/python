from django.shortcuts import render, redirect

from app.Blog import models
from app.user.models import User
from app.Blog.models import BlogInfo
# Create your views here.


def index(request):
    id = request.COOKIES.get('id')
    # print(id)
    user = User.objects.get(id=id)
    # print(user.id)
    blogs = BlogInfo.objects.filter(Buser=user.id)
    # print(blogs)
    if len(blogs) != 0:
        context = {'user': user,'blogs':blogs}
        return render(request, 'blog.html', context)
    else:
        context = {'user':user}
        return render(request,'blog.html',context)


def new(request):
    return render(request,'newblog.html')


def write(request):
    bloginfo = BlogInfo()
    bloginfo.title = request.POST.get('title')
    bloginfo.content = request.POST.get('context')
    bloginfo.Buser_id = request.COOKIES.get('id')
    bloginfo.save()
    return redirect('/blog/')


def lk(request,id):
    blog = BlogInfo.objects.get(id=id)
    return render(request,'newblog.html',{'blog':blog})


def dell(request,id):
    models.BlogInfo.objects.filter(id=id).delete()
    return redirect('/blog/')


def modify(request,id):
    blog = BlogInfo.objects.get(id=id)
    blog.title = request.POST.get('title')
    blog.content = request.POST.get('context')
    blog.save()
    return redirect('/blog/')
