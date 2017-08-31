from django.db import models

class Category(models.Model):
	name = models.CharField(max_length=200, unique=True) 	# unique设置为True时，以为这name的值必须为唯一值。也就是说你可以将name作为数据库的主键(primary key)
	views = models.IntegerField(default=0)
	likes = models.IntegerField(default=0)
	class Meta:
		verbose_name_plural = 'Categories'

	def __str__(self):
		return self.name

class Page(models.Model):
	category = models.ForeignKey(Category)
	title = models.CharField(max_length=128)
	url = models.URLField()
	views = models.IntegerField(default=0)

	def __str__(self):
		return self.title