from django.db import models

# Create your models here.    创建模型，创建之后需要注册

class Gallery(models.Model):
    description = models.CharField(default="描述",max_length=100)
    image = models.ImageField(default="default.png",upload_to="image/")
    title = models.CharField(default="标题",max_length=50)

    def __str__(self):
        return self.title