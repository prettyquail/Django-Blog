from django.db import models

# Create your models here.
class BlogApp(models.Model):
	title=models.CharField(max_length=88)
	description=models.TextField(blank=False)
	author=models.CharField(max_length=20)
	date=models.DateField(auto_now_add=True)

	
