from django.db import models
from datetime import datetime
# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=30)
    emp_num = models.IntegerField(unique=True)
    password = models.CharField(max_length=64)

    def __str__(self):
        return self.username

class Depart(models.Model):
    depart_name =models.CharField(max_length=30)

    def __str__(self):
        return self.depart_name

class Record(models.Model):
    record_text = models.CharField(max_length=100)
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    depart = models.ForeignKey(Depart,on_delete=models.CASCADE)
    detail_text = models.CharField(max_length=100)
    record_comment= models.CharField(max_length=100,null=True)
    record_time=models.DateField(datetime.now())

    def __str__(self):
        return '[{}]{}{}{}'.format(self.record_text,self.username,self.depart,self.record_time)

class Log(models.Model):
    time = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    record = models.ForeignKey(Record,on_delete=models.CASCADE,null=True)
    action = models.CharField(max_length=30)
    class Meta:
        verbose_name = 'Log'
        verbose_name_plural = verbose_name
        ordering =['id']

    def __str__(self):
        return '[{}]{}{}{}'.format(self.time, self.user, self.record, self.action)
