from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Matrix(models.Model):
	# set the field to now when the object is first created
	timestamp = models.DateTimeField(auto_now = False, auto_now_add = True)
	
	# set the field to now every time the object is saved
	updated = models.DateTimeField(auto_now = True, auto_now_add = False)
	
	# what is your file system
	filesys = models.CharField(max_length = 120)

	# what is your benchmark
	bench = models.CharField(max_length = 120)

	# what is your matrixs
	mx1 = models.FloatField(blank = True)
	mx2 = models.FloatField(blank = True)
	mx3 = models.FloatField(blank = True)
	mx4 = models.FloatField(blank = True)
	#mx5 = models.FloatField(blank = True)
	#mx6 = models.FloatField(blank = True)
	#mx7 = models.FloatField(blank = True)
	#mx8 = models.FloatField(blank = True)

	def __unicode__(self):
		return  self.filesys, self.bench 