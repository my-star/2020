from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
class Depart(models.Model):
    Depart_name = models.CharField(max_length=20)

    def __str__(self):
        return self.Depart_name

class Record(models.Model):
    record_num = models.CharField(max_length=30)
    title = models.CharField(max_length=50)
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    depart = models.ForeignKey(Depart,on_delete=models.CASCADE)
    record = models.TextField()
    record_time =models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
