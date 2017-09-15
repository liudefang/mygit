#coding=utf-8
from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from django import forms

# Create your views here.
from bookapp.models import User


class UserForm(forms.Form):
    account = forms.CharField(label='用户名',max_length=50)
    password = forms.CharField(label='密码',widget=forms.PasswordInput())
    email = forms.EmailField(label='邮箱')

def regist(request):
    if request.method == 'POST':
        userform = UserForm(request.POST)
        if userform.is_valid():
            account = userform.cleaned_data['account']
            password = userform.cleaned_data['password']
            email = userform.cleaned_data['email']

            '''User.objects.create(account=account,password=password,email=email)
            User.save()'''
            # 将表单写入数据库
            user = User()
            user.account = account
            user.password = password
            user.email = email
            user.save()

            return render_to_response('success.html',{'account':account})
    else:
        userform = UserForm()
    return render_to_response('regist.html',{'userform':userform})

def login(request):
    if request.method == 'POST':
        userform = UserForm(request.POST)
        if userform.is_valid():
            account = userform.cleaned_data['account']
            password = userform.cleaned_data['password']

            user = User.objects.filter(account__exact=account,password__exact=password)

            if user:
                return render_to_response('index.html',{'userform':userform})
            else:
                return HttpResponse('用户名或密码错误,请重新输入')


    else:
        userform = UserForm()
    return render_to_response('login.html',{'userform':userform})


def index():
    return render_to_response('index.html')