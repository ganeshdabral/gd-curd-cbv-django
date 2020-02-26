from django.db import models
from django.utils.encoding import smart_text
from django.db.models.signals import pre_save, post_save
from django.urls import reverse
from slugify import slugify
import random

class BookModel(models.Model):
	isbn = models.IntegerField(unique=True, null=True)
	title = models.CharField(max_length=150, null=True)
	slug = models.SlugField(max_length=250, unique=True, null=True, blank=True)
	description = models.CharField(max_length=500, null=True)
	author = models.CharField(max_length=150, null=True)
	page = models.IntegerField(null=True)
	created_at = models.DateField(auto_now_add=True)
	updated_at = models.DateField(auto_now=True)
	
	def __str__(self):
		return smart_text(self.title)

	def getAbsUrl(self):
		return reverse("detail_view", kwargs={"slug": self.slug})

	def getUpdateUrl(self):
		return reverse("update_view", kwargs={"slug": self.slug})

	def getDeleteUrl(self):
		return reverse("delete_view", kwargs={"slug": self.slug})

def pre_save_book_slug(sender, instance, *args, **kwargs):
	if instance.title and instance.slug is None:
		while(True):
			rendom_str = ''.join(str(random.randint(0, 9)) for _ in range(8))
			slug = slugify(instance.title +" "+str(rendom_str))
			qs = BookModel.objects.filter(slug=slug)
			if qs.count()==0:
				instance.slug = slug
				break		

pre_save.connect(pre_save_book_slug, sender=BookModel)