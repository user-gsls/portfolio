from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(default='文章标题',max_length=20)
    date = models.DateField()
    image = models.ImageField(default='default.png',upload_to='images/')
    text = models.TextField(default='文章内容')

    def __str__(self):
        return self.title
