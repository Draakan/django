# -*- coding: utf-8 -*-

from django.db import models

class Exam(models.Model):

	class Meta(object):
		verbose_name = u"Екзамен"
		verbose_name_plural = u"Екзамени"
	
	name = models.CharField(
		max_length=256,
		blank=False,
		verbose_name=u"Назва")
		
	date_and_time = models.DateTimeField(
		blank=False,
		verbose_name = u"Дата і час")
	
	teacher = models.CharField(
		max_length=256,
		blank=False,
		verbose_name = u"Викладач")
		
	group = models.OneToOneField('Group',
		verbose_name = u"Група",
		blank=False,
		null = True,
		on_delete = models.SET_NULL)
		
	notes = models.TextField(
		blank=True,
		verbose_name=u"Додаткові нотатки")
		
	def __unicode__(self):
		return u"%s %s %s" % (self.teacher, self.name, self.group)
