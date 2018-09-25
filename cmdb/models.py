from django.db import models

# Create your models here.
# 建表到mysql，在terminal再执行下manage.py ...
class Test(models.Model):
    name = models.CharField(max_length=20)

class Contact(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField(default=0)
    email = models.EmailField()
    def __unicode__(self):
        return self.name
# Tag表以Contact为外键，一个Contact可以对应多个Tag
class Tag(models.Model):
    contact = models.ForeignKey(Contact,on_delete=models.CASCADE)
    # on_delete=models.CASCADE要加，避免两个表里的数据不一致问题
    name = models.CharField(max_length=50)
    def __unicode__(self):
        return  self.name