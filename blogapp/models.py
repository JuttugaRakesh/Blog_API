from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=50,null=True,blank=True)
    content = models.TextField(null=True,blank=True)
    date_created = models.DateTimeField(default=datetime.now, blank=True )
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title



