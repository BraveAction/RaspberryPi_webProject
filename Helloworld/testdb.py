# -*- coding: utf-8 -*-

from django.http import HttpResponse

from people.models import Person


# 数据库操作
def testdb(request):
    person = Person(name='runoob', age=13)
    person.save()
    return HttpResponse("<p>数据添加成功！</p>")
