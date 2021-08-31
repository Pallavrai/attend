from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from account.models import Profile
from django.db.models.fields import DateField, IntegerField
import datetime
import ast

class attendmonth(models.Model):
    student=models.ForeignKey(User,on_delete=CASCADE)
    date=models.DateField(auto_now=True)
    attended=models.BooleanField(default=False)

    def __str__(self):
        return str(self.date)

    def save(self,*args,**kwargs):
        
        mydate = datetime.datetime.now()
        month=mydate.strftime("%B")
        data=Profile.objects.get(user=self.student)
        
        res=ast.literal_eval(data.total_attended)
        try:
            res[month]=res[month]+1
        except:
            res[month]=1
        data.total_attended=str(res)

        data.save()
        super(attendmonth,self).save(*args,**kwargs)
    