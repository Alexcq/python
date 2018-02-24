from django.core.exceptions import FieldError
import json
from django.shortcuts import render, redirect
from django.http import HttpResponse , HttpResponseRedirect
from app.Blog.models import BlogInfo
from app.user.models import User

# Create your views here.


def index(request):
    return render(request, 'zc.html')


def zc(request):
    zcxx = request.POST
    zc_name = zcxx.get('username')
    # if len(zc_name) > 20:
    #     # raise FieldError("name is too long")
    #     return HttpResponse("name is too long")
    zc_pwd = zcxx.get('pwd')
    zc_pwd1 = zcxx.get('pwd1')
    if zc_pwd == zc_pwd1 and zc_pwd != "" :
        # 写入数据库
        user = User()
        user.name = zc_name
        user.pwd = zc_pwd
        user.save()
        context = {'name':zc_name,'pwd':zc_pwd}
        return render(request, 'zc_pass.html', context)
    else:
        return render(request, 'zc.html')


def dl(request):
    return render(request, 'login.html')


def login(request):
    dlxx = request.POST
    name = dlxx.get('username')
    pwd = dlxx.get('pwd')
    try:
        #尝试从缓存中获取
        #缓存中存的是String
        #需要将String转为user
        #用到json lib
        # userInfoString = redis.get(name) #{name:'aaa',psw='qwe'}
        # if (userInfoString != null):
        #     user = json.from(userInfoString)
        # if (user != null):
        #

        user = User.objects.get(name=name)
        users = User.objects.values()
        for x in users:
            if x['name'] == name :
                print(x)
                userInfo = json.dumps(x)
                userinfo = json.loads(userInfo)
                print('1',userInfo)
                print('2',userinfo)
        # print(users)
        # userInfoString = json.dumps("json", user.to_dict())
        # print(userInfoString)
        if user:
            upwd = user.pwd
            if upwd == pwd:
                response = HttpResponseRedirect('/blog/')
                response.set_cookie('id',user.id)
                # print(user.id)
                return response
            else:
                print("密码错误")
                return render(request, 'login.html')
        else:
            print("没有账号")
            return render(request, 'login.html')
    except BaseException as e:
        print(e)
        return render(request, 'login.html')

