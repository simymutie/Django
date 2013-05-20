from django.db import models
from string import join
from easy_thumbnails.signals import saved_file
from easy_thumbnails.signal_handlers import generate_aliases_global
import easy_thumbnails
from easy_thumbnails.fields import ThumbnailerImageField 
from django.contrib.auth.models import User
from django.contrib import admin
from django.db import models

class Category(models.Model):
	tag = models.CharField(max_length=100)
	
	def __unicode__(self):
		return self.tag

class HomePage(models.Model):
	title		= models.CharField(max_length=150)
	category	= models.ManyToManyField(Category, blank=True)
	date		= models.DateTimeField(auto_now_add=True)
	image = ThumbnailerImageField(upload_to = "images/thumbnails", blank=True, resize_source=dict(size=(200,200), sharpen=True))
	content		= models.TextField(blank=False)
	class Meta:
		get_latest_by =('date')
	def thumbnail(self):
		return """<a href="/media/%s"><img border="0" alt="" src="/media/%s" height="40" /></a>""" % (
													(self.image.name, self.image.name))
	thumbnail.allow_tags = True
	
	def category_(self):
		lst = [x[1] for x in self.category.values_list()]
		return str(join(lst, ', '))
    
        def __unicode__(self):
		return self.title
		
saved_file.connect(generate_aliases_global)
        
        
    
