from django.db import models

"""
    创建应用程序数据表模型（对应数据库的相关操作）
    M 代表模型（Model）
    模型的每个属性都表示为数据库中的一个字段
    Django 提供一套自动生成的用于数据库访问的API；
"""


# Create your models here.
# 发布会表
class Event(models.Model):
    name = models.CharField(max_length=100)  # 发布会标题
    limit = models.IntegerField()            # 参加人数
    status = models.BooleanField()           # 状态
    address = models.CharField(max_length=200)            # 地址
    start_time = models.DateTimeField('events time')      # 发布会时间
    create_time = models.DateTimeField(auto_now=True)    # 创建时间（自动获取当前时间）

    def __str__(self):
        return self.name


# 嘉宾表
class Guest(models.Model):
    event = models.ForeignKey(Event)              # 关联发布会id
    realname = models.CharField(max_length=64)    # 姓名
    phone = models.CharField(max_length=16)       # 手机号
    email = models.EmailField()                   # 邮箱
    sign = models.BooleanField()                  # 签到状态
    create_time = models.DateTimeField(auto_now=True)  # 创建时间（自动获取当前时间）

    class Meta:
        unique_together = ("event", "phone")

    def __str__(self):
        """__str__()方法告诉Python 如何将对象以str 的方式显示出来"""
        return self.realname
