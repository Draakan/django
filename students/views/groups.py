# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse
from datetime import datetime
from django.views.generic import UpdateView, DeleteView
from django.forms import ModelForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.bootstrap import FormActions

from ..models import Student
from ..models import Group

def groups_list(request):
    groups = Group.objects.all()
    
    order_by = request.GET.get('order_by', '')
    if order_by in ('title', 'leader'):
        groups = groups.order_by(order_by)
        if request.GET.get('reverse', '') == '1':
            groups = groups.reverse()
            
    paginator = Paginator(groups, 3)
    page = request.GET.get('page')
    try:
    	groups = paginator.page(page)
    except PageNotAnInteger:
    	groups = paginator.page(1)
    except EmptyPage:
    	groups = paginator.page(paginator.num_pages)
     
    return render(request, 'students/groups_list.html',
        {'groups': groups})

def groups_add(request):
    return HttpResponse('<h1>Group Add Form</h1>')

def groups_edit(request, gid):
    return HttpResponse('<h1>Edit Group %s</h1>' % gid)

class GroupDeleteView(DeleteView):
	model = Group
	template_name = 'students/groups_confirm_delete.html'
	
	def get_success_url(self):
		return u'%s?status_message=Групу успішно видалено' % reverse('groups')
