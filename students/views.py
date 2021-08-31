from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import JsonResponse
from account.models import Profile
import ast
import json
# Create your views here.
@login_required
def home(request,id=None):
    data=None
    profile=None
    usr=User.objects.all()
    try:
        if id is not None:
            global uid
            uid=id
            profile=Profile.objects.filter(user=id)
            data=list(Profile.objects.filter(user=id).values('total_attended'))[0]
            
        else:
            profile=Profile.objects.filter(user=request.user)
            data=list(Profile.objects.filter(user=request.user).values('total_attended'))[0]
        data=ast.literal_eval(data['total_attended'])
        data=json.dumps(data)
    except:
        messages.error(request,"Sorry We Don't have this record yet.")

        
    context={
        'name':usr,
        'data':data,
        'profile':profile,
    }
    return render(request,'students/home.html',context)


# def generate(request,id):
#     global uid
#     uid=id
#     data=list(Profile.objects.filter(user=request.user).values('total_attended'))[0]
#     print(request.user)
#     data=ast.literal_eval(data['total_attended'])
#     return JsonResponse(data)




def delete(request):
    if uid:
        User.objects.filter(pk=uid).delete()
        print(uid)
    return redirect('home')
