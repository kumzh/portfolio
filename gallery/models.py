from django.db import models

# Create your models here.    创建模型，创建之后需要注册

class Gallery(models.Model):
    description = models.CharField(max_length=100)