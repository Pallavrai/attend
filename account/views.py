from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method == 'POST':
      form = UserCreationForm(request.POST)
      if form.is_valid(): 
        form.save()
        return redirect('home')
    else:
      form = UserCreationForm()

    context={'form':form}
    return render(request,'account/register.html',context)

def login_usr(request):
    if request.user.is_authenticated:
      return redirect('/')
    if request.method=='POST':
      usr=request.POST['username']
      pwd=request.POST['pwd']
      user=authenticate(request,username=usr,password=pwd)
      if user is not None:
        login(request,user)
        return redirect('/')
      else:
        messages.error(request,'Wrong ID or Password')    
    return render(request,'account/login.html')

def logout_usr(request):
    logout(request)
    return redirect('/login')