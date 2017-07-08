from django.shortcuts import render
from PdoApp import  models
# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from django.http import HttpResponse
def LOGIN(request):
    return render(request,'background.html')
def index(request):
    return render(request,'index.html')
def zhuce(request):
    return render(request,'PersonInfo.html')
def xiugai(request):
    return render(request,'modify.html')
def regist(request):
    admin = request.GET['a']
    password = request.GET['b']
    repassword = request.GET['c']
    if not admin:
        return HttpResponse(u"用户名不能为空")
    list = models.Admincheck.objects.filter()
    for i in list:
        d = str(i.admin)
        e = str(i.password)
        if password != repassword:
            return HttpResponse(u"两次密码不一致,请返回上一页面重新注册")
        if admin == d:
            return HttpResponse(u"用户名已存在")
    p =models.Admincheck(admin=admin)
    p.password = password
    p.save()
    return render(request, 'background.html')
def home(request):
    personlist = models.Information.objects.filter()
    return render(request,'home.html', {'personlist': personlist})
def information(request):
    personlist = models.Information.objects.filter()
    for i in range(len(personlist)):
        if count ==str(personlist[i].map):
            int(i);
            return render(request,'userInfo.html', {'personlist': personlist[i]})

def nav(request):
    return render(request,'nav.html')
def add(request):
        admin = request.GET['a']
        password = request.GET['b']
        admin = str(admin)
        global count
        count = str(admin)
        password = str(password)
        list = models.Admincheck.objects.filter()
        for i in list:
            d = str(i.admin)
            e = str(i.password)
            if admin == d:
                if password == e:
                     #return HttpResponse(u"信息分析团队欢迎你")
                    personlist = models.Information.objects.filter()
                    #response = HttpResponseRedirect('')
                  # return  render(request, 'nav.html')
                   # response.set_cookie('admin', admin, 3600)
                    #return response
                    return render(request, 'nav.html')
                else:
                    return HttpResponse(u"密码错误 ：（")
            else:
                continue
        return HttpResponse(u"用户名不存在 ：（")


def modify(request):
    oldpassword = request.GET['a']
    newpassword = request.GET['b']
    repassword = request.GET['c']
    if newpassword != repassword:
        return HttpResponse(u"两次密码不一致,请返回上一页面重新修改")
    personlist = models.Admincheck.objects.filter()
    for i in range(len(personlist)):
        if count == str(personlist[i].admin):
            break;
    if oldpassword !=personlist[i].password:
        return HttpResponse(u"旧密码输入有误,请返回上一页面重新修改")
    models.Admincheck.objects.filter(admin=count).update(password=newpassword)
    return HttpResponse(u"修改成功,请重新登录")
