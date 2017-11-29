from django.db import models

# Create your models here.
class UserGroup(models.Model):
    uid = models.AutoField(primary_key=True)
    caption = models.CharField(max_length=32,unique=True)
    ctime = models.DateTimeField(auto_now_add=True,null=True)
    upime = models.DateTimeField(auto_now=True,null=True)

# 表名 app01_userinfo

class UserInfo(models.Model):
    # 自动创建ID列，自增属性，主键
    # 创建用户名列，字符串类型，指定长度
    # 字符串、时间、数字、二进制
    username = models.CharField(max_length=32, verbose_name='用户名',help_text='输入用户名',error_messages={'invalid':'请输入用户名'})
    password = models.CharField(max_length=64, verbose_name='密码',help_text='输入密码',error_messages={'invalid':'输入密码'})
    email = models.EmailField(max_length=255, verbose_name='邮箱', help_text='填写邮箱', error_messages={'invalid':'请填写邮箱'}, null=True)
    other = models.CharField(max_length=255, verbose_name='备注', help_text='填写备注', error_messages={'invalid':'请填写备注'}, null=True, )
    # user_group_id 是数字
    user_group = models.ForeignKey("UserGroup", to_field='uid', default=1) # 封装信息 (uid,caption,ctime.uptime)
    user_type_choices = (
        (1,'超级用户'),
        (2,'贵宾用户'),
        (3,'普通用户')
    )
    user_type_id = models.IntegerField(choices=user_type_choices,default=1,verbose_name='用户类型',help_text='选择用户类型')