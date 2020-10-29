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


class UserProfile(models.Model):

    PRIVACY = (
        ('private' , 'private'),
        ('public' , 'public'),
    )
    user = models.ForeignKey(User , on_delete = models.CASCADE)
    bio = models.TextField()
    privacy = models.CharField(max_length = 20 , choices = PRIVACY , default = "public")
    image = models.ImageField(upload_to = "profile_pics" , default = "image.jpg")


    def __str__(self):

        return f'{self.user.username} profile'


class Updates(models.Model):

    pass