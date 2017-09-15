from django.contrib import admin
from django.db import models

# Create your models here.
class Book(models.Model):
    class Meta:
        verbose_name = '图书'
        verbose_name_plural = verbose_name

    isbn = models.CharField('ISBN', max_length=13, unique=True)
    title = models.CharField('书名', max_length=200)
    subtitle = models.CharField('副标题', max_length=200, blank=True)
    pages = models.IntegerField('页数', blank=True)
    author = models.CharField('作者', max_length=60)
    translator = models.CharField('译者', max_length=60, blank=True)
    price = models.CharField('定价', max_length=60, blank=True)
    publisher = models.CharField('出版社', max_length=200, blank=True)
    pubdate = models.CharField('出版日期', max_length=60, blank=True)
    cover_img = models.URLField('封面图', blank=True)
    summary = models.TextField('内容简介', blank=True, max_length=2000)
    author_intro = models.TextField('作者简介', blank=True, max_length=2000)

class Reader(models.Model):
    account = models.CharField(max_length=64)  # 账号
    name = models.CharField(max_length=64)  # 姓名
    email = models.CharField(max_length=128)  # 邮箱
    contact = models.IntegerField(max_length=16)  # 联系方式

    def __unicode__(self):
        return self.account

class User(models.Model):
    account = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField()

class UserAdmin(admin.ModelAdmin):
    list_display = ('account','password','email')

admin.site.register(User,UserAdmin)