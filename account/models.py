from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=CASCADE)
    pic=models.ImageField(upload_to='profile_pic')
    total_attended=models.TextField(default='{"Jan":31,"Feb":28,"Mar":31,"Apr":30,"May":31,"Jun":30,"Jul":31,"Aug":31,"Sept":30,"Oct":31,"Nov":30,"Dec":31}')

    def __str__(self):
        return str(self.user)


