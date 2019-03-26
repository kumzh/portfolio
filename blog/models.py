from django.db import models

# Create your models here.
from django.views.generic import TemplateView
DJANGO_ECHARTS = {
    'echarts_version': '4.0.4',
    'lib_js_host':'cdnjs'
}


class Blog(models.Model):
    title = models.CharField(default="文章标题",max_length=50)
    date = models.DateField()
    image = models.ImageField(default="default.png",upload_to="image/")
    text = models.TextField(default="文章正文")
    def __str__(self):
        return self.title

    def description(self):
        return self.text[:100] + '....'

