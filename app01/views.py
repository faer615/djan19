from django.shortcuts import render, redirect, HttpResponse

# Create your views here.

def login(request): # 用户登陆
#    models.UserGroup.objects.create(caption='DBA')

    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        # 数据库中执行 select * from user where username='user' and password='password'
        u = request.POST.get('user')
        p = request.POST.get('pwd')
        # e = request.POST.get('email')
        # o = request.POST.get('other')
        # obj = models.UserInfo.objects.filter(username=u,password=p).first() # 首选
        # print(obj) # if obj None,无此用户
        # count = models.UserInfo.objects.filter(username=u, password=p).count() # 大于0，有此用户
        # obj = models.UserInfo.objects.filter(username=u, password=p, email=e, other=o).first()
        obj = models.UserInfo.objects.filter(username=u, password=p).first()
        if obj:
            return redirect('/cmdb/index/')
        else:
            return render(request, 'login.html')
    else:
        # 提交方式 PUT,DELETE,HEAD,OPTION...
        return redirect('/index/')

def index(request): # 返回首页
    return render(request, 'index.html')

def user_info(request): # 显示用户信息
    if request.method == "GET":
        user_list = models.UserInfo.objects.all()
        group_list = models.UserGroup.objects.all()
        # for row in user_list:
        #     print(row.id)
        #     print(row.user_group.uid)
        #     print(row.user_group.caption)
        # print(user_list.query)
        # QuerySet 包含[obj(id,username,email,user_group_id(uid,caption),obj]
        return render(request,'user_info.html', {'user_list':user_list, 'group_list':group_list})
    elif request.method == "POST": # 添加用户
        u = request.POST.get('user')
        p = request.POST.get('pwd')
        # e = request.POST.get('email')
        # o = request.POST.get('other')
        models.UserInfo.objects.create(username=u,password=p)
        # models.UserInfo.objects.create(username=u,password=p, email=e, other=o)
        return redirect('/cmdb/user_info/')

def user_detail(request, nid): # 显示用户详细信息
    obj = models.UserInfo.objects.filter(id=nid).first()
    # 获取单条数据,如果不存在，直接报错
    # models.UserInfo.objects.get(id=nid)
    return render(request, 'user_detail.html', {'obj':obj})

def user_del(request,nid): # 删除用户
    models.UserInfo.objects.filter(id=nid).delete()
    return redirect('/cmdb/user_info/')

def user_edit(request,nid): # 编辑用户
    if request.method == "GET":
        obj = models.UserInfo.objects.filter(id=nid).first()
        print(obj.id)
        return render(request,'user_edit.html',{'obj':obj})
    elif request.method == "POST":
        nid = request.POST.get('id')
        u = request.POST.get('username')
        p = request.POST.get('password')
        # e = request.POST.get('email')
        # o = request.POST.get('other')
        obj = models.UserInfo.objects.filter(id=nid).update(username=u,password=p)
        print(obj)
        return redirect('/cmdb/user_info/')

from app01 import models
def orm(request):
    # 创建数据
    # models.UserInfo.objects.create(username='root', password='king111')

    # dic = {'username':'zheng', 'password':'king111'}
    # models.UserInfo.objects.create(**dic)

    #obj = models.UserInfo(username='xiao', password='king111')
    #obj.save()

    # 查询语句
    # result = models.UserInfo.objects.all() # 获取所有数据
    # result = models.UserInfo.objects.filter(username='root') # 条件查询
    # result 是 Django 提供的 QuerySet，获取到的数据是UserInfo的对象
    # for row in result:
    #     print(row.id, row.username, row.password)
    # print(result)

    # 删除语句
    # models.UserInfo.objects.filter(id=4).delete()

    # 更新语句
    # models.UserInfo.objects.all().update(password='king123')
    # models.UserInfo.objects.filter(id=2).update(password='king111')

    # 一对多
    # user_list = models.UserInfo.objects.all()

    # models.UserInfo.objects.create(
    #     username='root1',
    #     password='111111',
    #     email='root1@root.com',
    #     other='beizhu',
    #     user_group = models.UserInfo.objects.filter(id=1).first()
    # )

    models.UserInfo.objects.create(
        username='root1',
        password='111111',
        email='root1@root.com',
        other='beizhu',
        user_group_id = 1
    )

    return HttpResponse('orm')

# def home(request):
#     return HttpResponse('Home')

from django.views import View
class Home(View):
    def dispatch(self, request, *args, **kwargs):
        # 调用父类的dispatch 助理作用
        print('before')
        result = super(Home, self).dispatch(self, request, *args, **kwargs)
        print('after')
        return result

    def get(self, request):
        print(request.method)
        return render(request, 'home.html')

    def post(self, request):
        print(request.method, 'POST')
        return render(request, 'home.html')