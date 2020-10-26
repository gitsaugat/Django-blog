from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone 

class Post(models.Model):

    content = models.TextField()
    title   = models.CharField(max_length = 300)
    user    =  models.ForeignKey(User , on_delete = models.CASCADE)
    date_published = models.DateTimeField(default = timezone.now())


    def __str__(self):

        return self.title 


        

