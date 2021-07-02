from django.db import models

# Create your models here.
class Department(models.Model):
    depart_name = models.CharField(max_length=50)
    def __str__(self):
        return self.depart_name

class MatUser(models.Model):
    user_name = models.CharField(max_length=50)
    emp_num = models.IntegerField()
    tel = models.IntegerField(blank=True)
    id_num = models.IntegerField(blank=True)
    address = models.CharField(blank=True,max_length=100)
    depart = models.ForeignKey(Department,on_delete=models.DO_NOTHING)
    def __str__(self):
        return self.user_name

class Computer(models.Model):
    computer_num = models.CharField(max_length=50)
    computer_user = models.ForeignKey(MatUser,on_delete=models.DO_NOTHING)
    computer_name = models.CharField(max_length=50)
    buy_time = models.DateField()
    location = models.CharField(blank=True,max_length=100)
    def __str__(self):
        return self.computer_name