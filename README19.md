#  Django 学习笔记 daascmdb 项目
### 第19天 创建于 2017年11月20日 --- 完成于28日

## 一、web框架
    MVC
    Model View Controller
    数据库 模板  业务处理
---
## MTV
    Model Template View
    数据库 模板  业务处理
---
## Django 框架

    pip3.6 install django
    django-admin startproject mysite (工程名称)

    - mysite        # 对整个程序进行配置
        - init
        - settings  # 配置文件
        - url       # url对应关系
        - wsgi      # 遵循WSGI规范，uwsgi + nginx
    - manage.py     # 管理Django程序：
                      - python manage.py
                      - python manage.py startapp xxx 创建app应用
                      - python manage.py makemigrations 生成数据库
                      - python manage.py migrate 自动生成表
---
## 运行jdango服务
    python3.6 manage.py runserver 127.0.0.1:8001
---
## 网站
    - 前台
        - 配置
    - 主站     app
    - 后台管理  app
---
## 创建 app
    python manage.py startapp cmdb
    python manage.py startapp app名称
---
### app目录结构说明 (可以自动修改数据库类型)
    migrations  数据库修改结构
    admin       Django的后台管理
    apps        配置当前app
    models      ROM，写指定的类，通过命令可以创建数据库结构
    tests       单元测试
    views       业务代码 （实际代码位置）
---
### 1.配置模板路径
    主文件目录 设置 settings.py 文件
    
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [os.path.join(BASE_DIR, 'templates')] # 模板路径
            ,
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        },
    ]
---  
### 2.配置静态模板
  主文件目录在 settings.py 文件最后添加
  
    STATIC_URL = '/static/'
    STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
    )
---
### 3.注释掉settings.py 报错 csrf
     # 'django.middleware.csrf.CsrfViewMiddleware',
---
## 内容汇总
### 1.创建Django工程
      django-admin startproject 工程名
---
### 2.创建app
      cd 工程名
      python manage.py startapp cmdb
---        
### 3.静态文件
     porject.settings.py
        STATICFILES_DIRS = (
            os.path.join(BASE_DIR, "static")
        )
---        
### 4.模板路径
      DIRS ==> [os.path.join(BASE_DIR,'templates'),]
---        
### 5.注释csrf
      settings --> middlerware 注释 # csrf
---     
### 6.定义路由规则
      url.py
        "login" --> 函数名
---       
### 7.定义视图函数
      app下views.py
          def func(request):
              # request.method GET / POST
              # request.GET.get('',None)  # 获取请求发来的元数据
              # request.POST.get('',None) post提交数据

              # return HttpResponse("字符串")
              # return render(request, "HTML模板路径")
              # return redirect("只能填写URL路径")
---                
### 8.模板渲染
#### (1)特殊的模板语言
        def func(request):
            # return render(request, "index.html", {'current_user':"felix"})
        
        index.html
        
        <html>
        ..
            <body>
                <div>{{ current_user }}</div>
            </body>
            </html>
---
#### (2) ===> 最后生成页面
        <html>
         ...
          <body>
              <div>felix</div>
          </body>
        </html>
---
#### (3) ===> for循环
        def func(request):
        	return render(request, "index.html", {'current_user': "alex", 'user_list': ['alex','eric']})

        	    index.html

        	<html>
        		..
        		<body>
        			<div>{{current_user}}</div>
        			<ul>
        				{% for row in user_list %}
        					{% if row == "alex" %}
        					    <li>{{ row }}</li>
        					{% endif %}
        				{% endfor %}
        			</ul>
        		</body>
        	</html>
---      				
#### (4) *** 索引 取值 ***
        def func(request):
        	return render(request, "index.html", {
        				'current_user': "alex",
        				'user_list': ['alex','eric'],
        				'user_dict': {'k1': 'v1', 'k2': 'v2'}})

        index.html

        <html>
        ..
        	<body>
        		<div>{{current_user}}</div>
        		<a> {{ user_list.1 }} </a>
        		<a> {{ user_dict.k1 }} </a>
        		<a> {{ user_dict.k2 }} </a>
        	</body>
        </html>
---
#### (5) *** 条件 判断 ***
        def func(request):
        	return render(request, "index.html", {
        				'current_user': "alex",
        				"age": 18,
        				'user_list': ['alex','eric'],
        				'user_dict': {'k1': 'v1', 'k2': 'v2'}})

        index.html

        <html>
        ..
        	<body>
        		<div>{{current_user}}</div>
        		<a> {{ user_list.1 }} </a>
        		<a> {{ user_dict.k1 }} </a>
        		<a> {{ user_dict.k2 }} </a>
        		  {% if age %}
        			  <a>有年龄</a>
        			{% if age > 16 %}
        				<a>老男人</a>
        			{% else %}
        				<a>小鲜肉</a>
        			{% endif %}

        		{% else %}
        			<a>无年龄</a>
        		{% endif %}
        	</body>
        </html>
---
## 二、资源信息管理（cmdb）
### 1.数据库
        MySQL *
        SQLAlchemy
        8列以上
---
### 2.主机管理(8列数据)：
        ip地址
        端口号
        业务线
---
### 3.用户表：
        用户名
        密码
---
### 4.功能：
        1.登陆
        2.主机管理页面
            - 查看所有的主机信息(显示4列)
            - 增加主机信息(8列) ** 模态对话框 placeholder
        3.查看详情
            url:
                "detail" --> detail
            def detail(request):
                request.GET.get("nid")
                v = select * from tb where id = nid # 查询数据库
                ...
        4、删除
        	del_host -> delete_host
        	def delete_host(request):
        		nid = request.POST.get('nid')
        		delete from tb where id = nid
        		return redirect('/home')
---
### 其他功能
    1.用户组的增删改查
    2.用户怎删改查
      - 添加必须是对话框
      - 删除必须是对话框
      - 修改，必须显示默认值
      
    3.比较好看的页面
---

# 三、Django 框架学习
##  一、路由系统，url.py
### 1.一个url对应一个函数或者对应一个类
      url(r'^index/', views.index),
      url(r'^home/', views.Home.as_view()),
---      
### 2.一类url对应一个函数或者一个类
      url(r'^detail-(\d+).html', views.detail),
---      
### 3.根据正则表达式的分组进行匹配
      url(r'^detail-(?P<nid>\d+)-(?P<uid>\d+).html', views.detail),
      任意参数
      def detail(request, *args, **kwargs):
---
#### 实战：
#### a.
        url(r'^detail-(\d+)-(\d+).html', views.detail),

        def func(request, nid, uid)
            pass

        def func(request, *args):
            args = (2,9)

        def func(request, *args **kwargs):
            args = (2,9)
---
#### b.
        url(r'^detail-(?P<nid>\d+)-(?P<uid>\d+).html', views.detail),

        def func(request, nid, uid)
          pass

        def func(request, *kwargs):
            args = {'ind': 1, 'uid': 3}

        def func(request, *args **kwargs):
            args = (2,9)
---
### 4.name
      url：

        对url路由关系进行命名，以后可以根据此名称生成自己想要的url
           url(r'^index/', views.index, name='index'),
           url(r'^index/(\d+)/', views.index, name='index'),
           url(r'^buy/(?P<pid>\d+)/(?P<nid>\d+)/', views.index, name='i3'),
---
#### 视图views

	    def func(request, *args, **kwargs):
		    from django.urls import reverse

    			url1 = reverse('i1')                              # asdfasdfasdf/
    			url2 = reverse('i2', args=(1,2,))                 # yug/1/2/
    			url3 = reverse('i3', kwargs={'pid': 1, "nid": 9}) # buy/1/9/
---
#### 模板语言 templates
      xxx.html

      {% url "i1" %}               # asdfasdfasdf/
      {% url "i2" 1 2 %}           # yug/1/2/
      {% url "i3" pid=1 nid=9 %}   # buy/1/9/
---   
      模板语言对应:
      {% url "index" %}
      {% url "index" 1 %}
      当前url：
      request.path_info
---### 
### 5.路由分发
#### 主配置文件settings目录下添加url路由信息
       urlpatterns = [
            url(r'^cmdb/', include("app01.urls")),
            url(r'^monitor/', include("app02.urls")),
       ]
---
#### 在app目录中添加urls路由信息
       app01/urls.py
          from django.conf.urls import url,include
          from django.contrib import admin
          from app01 import views

       urlpatterns = [
          url(r'^login/', views.login),
       ]

#### 在app目录中添加urls路由信息
       app02/urls.py
         from django.conf.urls import url,include
         from django.contrib import admin
         from app02 import views

         urlpatterns = [
           url(r'^login/', views.login),
       ]
---
### 6.默认值
    待补充
---
### 7.命名空间
    待补充
---
## 二、视图函数 app.views.py
### 1.请求方法
    request.GET   # 获取数据
    request.POST  # 提交数据
    request.FILES
---
### 2.checkbox等多选内容
    request.POST.getlist()
---
### 3.上传文件,from标签添加 enctype="multipart/form-data" 设置
    obj = request.FILES.get('updata')
    import os
    file_path = os.path.join('updata', obj.name) # 定义上传路径
    f = open(file_path, mode='wb')
    for item in obj.chunks():
        f.write(item)
    f.close()
---		  
### 4. FBV (function base view) 函数基本视图
    CBV (class base view) 类基本视图

    url.py index --> 函数名
    view.py def 函数(request)

    ====>
    /index/ --> 函数名
    /index/ --> 类 --> 方法

    ====>
    建议：两者都用，根据支持框架选择
---
## 三、模板 *.html

---
## 四、ORM操作 数据库
select * from tb where id > 1

### 对应关系
    models.tb.objects.filter(id__gt=1)  # 大于1
    models.tb.objects.filter(id=1)      # 等于1
    models.tb.objects.filter(id__lt=1)  # 小于1
    
#### 一、创建类
####1. 根据类自动创建数据库表
     (a).创建类
        # 在app下的models.py文件添加
            from django.db import models
            
            # Create your models here.
            # 表名 app01_userinfo
            class UserInfo(models.Model):
                # 自动创建ID列，自增属性，主键
                # 创建用户名列，字符串类型，指定长度
                username = models.CharField(max_length=32)
                password = models.CharField(max_length=64)

     (b).settings文件 注册app
        INSTALLED_APPS = [
            'django.contrib.admin',
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.messages',
            'django.contrib.staticfiles',
            'app01',
        ]       
                
     (c).执行命令创建数据库
        python manage.py makemigrations
        python manage.py migrate
---
#### 字段的类型：
        字符串类型
        数字
        时间
        二进制
        自增（primary_key=True）
    
####  字段的参数：
        null                --> 值是否为空
        default             --> 默认值
        primary_key         --> 主键
        db_column           --> 列名
        db_index            --> 索引
        unique              --> 唯一索引
        unique_for_date     --> 只对时间做索引
        unique_for_month    --> 只对月做索引
        unique_for_year     --> 只对年做索引
        auto_now            --> 创建时，自动生成 
        auto_now_add        --> 更新时，自动更新为更新时间
        
        obj = UserGroup.objects.filter(id=1).update(caption='CEO') # 不生效
        obj = UserGroup.objects.filter(id=1).first()
        obj.caption = 'CEO'
        obj.save
        
        choices             --> django admin中显示下拉框，避免连表查询
        blank               --> django admin中是否为空
        verbose_name        --> django admin中显示中文
        editable            --> django admin禁止编辑
        error_messages      --> django admin自定义错误信息
        help_text           --> django admin帮助信息
        validators          --> django admin form 自定义验证错误信息       
---
### 设置为mysql数据库方法 ###
        DATABASES = {
            'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME':'daascmdb',
            'USER': 'root',
            'PASSWORD': 'king111',
            'HOST': '10.12.7.16',
            'PORT': '3306',
            }
        }
---
    *** 注意：python3 MySQL模块 ***
    a. Django 默认使用MySQL模块连接MySQL，可修改为pymysql
        在 settings 文件夹中 __init__.py 文件添加
        import pymysql
        
            pymysql.install_as_MySQLdb()
        
        安装pymysql
        pip install pymysql
    
    b. 或者pip install mysqlclient
---

       
#### 2. 根据类对数据库中的数据进行各种操作
        一对多：
            a.外键
            b.外键字段—_id
            c.models.tb.object.create(name='root',user_group_id=1)
            d. userlist = models.tb.object.all()
                for row in userlist:
                    row.id
                    row.user_group_id
                    rwo.user_group.caption
---

## 五、装饰器
    待补充

---
# 创建django项目
## 1.Django请求生命周期
    --> URL对应关系（匹配）  --> 视图函数 -->  返回用户字符串
    --> URL对应关系（匹配）  --> 视图函数 -->  打开一个HTML文件，读取内容
---
### 2.创建 Django project
    django-admin startproject mysite
    cd mysite
    python manage.py startapp cmdb
    ...
        mysite
          mysite
               - 配置文件
            - rul.py
            - settings.py
    
          cmdb
            - views.py
            - admin.py
            - models.py # 创建数据库表
---
### 3.配置
    模板路径
    静态文件路径
    # CSRF 注释掉
---
### 4.编写程序
    a. url.py
      /index/   --> func

    b. views.py
      def func(request):
          # 包含所有请求数据
          ...
          return HttpResponse('字符串') # 返回字符串
          return render(request, 'index.html',{'字典渲染'}) # 模板文件
          retrun redirect('URL') # 返回url
            
    c. 模板语言
        retrun render(request, 'index.html', {'li':[11,22,33]})

        {% for item in %}
            <h1>{{itme}}</h1>
        {% endfor %}

      *********** 索引用点 *************
      <h2> {{item.0 }} </h2>
---

# 其他知识
    method方法：
    http_method_names = ['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace']
    	
    GET:
        获取数据
    
    POST：
        提交数据
    
    class Foo:
    	pass
    	
    	def __str__(self):
    			retrun '123'
    			
    obj = Foo()
    print(obj)