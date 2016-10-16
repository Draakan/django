# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse

def students_list(request):
	students = (
		{'id': 1,
		  'first_name': u'Аднрій',
		  'last_name': u'Корост',
		  'ticket': 2123,
		  'image': 'img/podoba3.jpg'},
		 {'id': 2,
		   'first_name': u'Віталій',
		   'last_name': u'Подоба',
		   'ticket': 254,
		   'image': 'img/me.jpeg'},
		 {'id': 3,
		   'first_name': u'Тарас',
		   'last_name': u'Притула',
		   'ticket': 5332,
		   'image': 'img/piv.png'},
	)
	return render(request, 'students/students_list.html', 
		{'students': students})
	
def students_add(request):
	return HttpResponse('<h1>Student Add Form</h1>')
	
def students_edit(request, sid):
	return HttpResponse('<h1>Edit Student %s</h1>' % sid)
	
def students_delete(request, sid):
	return HttpResponse('<h1>Delete Student %s</h1>' % sid)

def groups_list(request):
	groups = (
		{'id': 1,
		  'name': u'МтМ-21',
		  'leader': {'id': 1, 'name': u'Тарас Мельник'}},
		{'id': 2,
		  'name': u'Мтм-22',
		  'leader': {'id': 2, 'name': u'Микола Садовський'}},
		{'id': 3,
		  'name': u'Мтм-23',
		  'leader': {'id': 3, 'name': u'Іванов Андрій'}},
		  
	)	
	return render(request, 'students/group_list.html', 
		{'groups': groups})
	
def groups_add(request):
	return HttpResponse('<h1>Group Add Form</h1>')
	
def groups_edit(request, gid):
	return HttpResponse('<h1>Edit Group %s</h1>' % gid)
	
def groups_delete(request, gid):
	return HttpResponse('<h1>Delete Group %s</h1>' % gid)
