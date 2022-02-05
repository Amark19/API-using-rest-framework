from django.db import models

# Create your models here.
class students(models.Model):
    stu_id = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=20)
    sname = models.CharField(max_length=20)
    std = models.CharField(max_length=20)
    def __str__(self):
        return self.fname