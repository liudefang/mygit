#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
Created on 2017/9/12 9:44
 
@author: 'mike.liu' 
'''

from bookapp.models import  Reader
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.http import HttpResponse, request

from django.shortcuts import render_to_response, get_object_or_404

'''''显示借阅人列表'''
def index(request):

    readers = Reader.objects.order_by('account')
    paginator = Paginator(readers,10)  #每页显示10行数据
    page = request.POST.get('pageNum',1)
    try:
        if int(page) > paginator.num_pages:
            page = str(paginator.num_pages)
        readers = paginator.page(page)
    except(EmptyPage,InvalidPage):
        readers = paginator.page(paginator.num_pages)
    return render_to_response('reader/basepage.html',{'readers':readers,'currentPage':page,'numPerPage':5})

'''添加借阅人信息'''
def addReader(rquest):

    if request.POST:
        account = request.POST.get('account', None)
        name = request.POST.get('name',None)
        email = request.POST.get('email',None)
        contact = request.POST.get('contact',None)
        '''验证借阅人是否已经存在'''
        readers = Reader.objects.filter(account_iexact = account)
        if readers:
            return HttpResponse({"status":201, "statusCode":201, "navTabId":request.POST.get('navTabId', 'readerindex'), "callbackType":request.POST.get('callbackType', None),
            "message":u'此账户已存在不能重复添加',"info":u'此账户已存在不能重复添加', "result":u'此账户已存在不能重复添加'}, mimetype='application/json')
        else:
            reader = Reader(account = account,name = name, email=email,contact=contact)
            reader.save()
            return HttpResponse(dumps({"statusCode":200, "navTabId":request.POST.get('navTabId', 'readerindex'), "callbackType":request.POST.get('callbackType', 'closeCurrent'), "message": u'添加成功'}), mimetype='application/json')

    return render_to_response('reader/add.html')

'''编辑借阅人信息'''
def editReader(request,id):
    reader = get_object_or_404(Reader,pk = int(id))
    if request.POST:
        reader.name = request.POST.get('name',None)
        reader.email = request.POST.get('email',None)
        reader.contact = request.POST.get('contact',None)
        reader.save()
        return HttpResponse({"statusCode":200, "navTabId":request.POST.get('navTabId', 'readerindex'), "callbackType":request.POST.get('callbackType', 'closeCurrent'), "menssage": u'编辑成功', "info": u'编辑成功', "result": u'编辑成功'}, mimetype='application/json')
    return render_to_response('reader/edit.html',{'reader':reader})

'''删除借阅人信息'''
def delReader(request,id):
    reader = Reader.objects.get(id = id)
    reader.delete()
    return HttpResponse({"statusCode":200, "navTabId":request.POST.get('navTabId', 'readerindex'), "callbackType":request.POST.get('callbackType', None), "message": u'删除成功', "info": u'删除成功', "result": u'删除成功'}, mimetype='application/json')

'''批量删除借阅人信息'''
def selectedelReader(request):
    ids = request.POST.get('ids',None)
    if ids:
        readers = Reader.objects.extra(where=['id IN(' + ids +')'])
        readers.delete()
        return HttpResponse(
            {"statusCode": 200, "navTabId": request.POST.get('navTabId', 'readerindex'),
             "callbackType": request.POST.get('callbackType', None), "message": u'删除成功', "info": u'删除成功',"result": u'删除成功'}, mimetype='application/json')

'''查询借阅人信息'''
def searchReader(request):
     if 'q' in request.POST and request.POST['q']:
         q = request.POST['q']
         readers = Reader.objects.filter(name__icontains = q)
     else:
         readers = Reader.objects.order_by('name')
     paginator = Paginator(readers,10)
     page = request.POST.get('pageNum',1)
     try:
         if int(page) > paginator.num_pages:
             page = str(paginator.num_pages)
         readers = paginator.page(page)
     except(EmptyPage,InvalidPage):
         readers = paginator.page(paginator.num_pages)
     if 'q' in request.POST and request.POST['q']:
         return render_to_response('reader/basepage.html',{'readers':readers,'currentPage':page,'numPerPage':5,'q':q})
     else:
          return render_to_response('reader/basepage.html',{'readers':readers,'currentPage':page,'numPerPage':5})