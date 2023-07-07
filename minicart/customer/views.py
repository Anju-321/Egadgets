from django.shortcuts import render,redirect
from django.http import HttpResponse 
from django.views.generic import View,CreateView,FormView
from .forms import RegForm,Logform
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
# Create your views here.

# Decorator
def signin_required(fn):
    def inner(request,*args,**kwargs):
        if request.user.is_authenticated:
            return fn(request,*args,**kwargs)
        else:
            messages.error(request,'login required')
            return redirect('logv')
    return inner

# Create your views here.

# class Regview(View):
#     def get(self,request):
#         form=RegForm()
#         return render(request,'reg.html',{'form':form})
#     def post(self,request):
#         form_data=RegForm(data=request.POST)
#         if form_data.is_valid():
#             form_data.save()
#             return redirect("logv")
#         else:
#             return render(request,'reg.html',{'form':form_data})

class Regview(CreateView):
    template_name='reg.html'
    form_class=RegForm
    success_url=reverse_lazy('logv')
    

# class LogView(View):
#     def get(self,request):
#         form=Logform()
#         us=request.user
#         return render(request,'log.html',{'form':form,'user':us})
#     def post(self,request):
#         form_data=Logform(data=request.POST)
#         if form_data.is_valid():
#             user=form_data.cleaned_data.get('username')
#             pswd=form_data.cleaned_data.get('password')
#             user_ob=authenticate(request,username=user,password=pswd)
#             if user_ob:
#                 login(request,user_ob)
#                 return redirect('Home')
#             else:
#                 return render(request,'log.html',{'form':form_data})

class LogView(FormView):
    template_name='log.html'
    form_class=Logform
    def post(self,request):
        form_data=Logform(data=request.POST)
        if form_data.is_valid():
            user=form_data.cleaned_data.get('username')
            pswd=form_data.cleaned_data.get('password')
            user_ob=authenticate(request,username=user,password=pswd)
            if user_ob:
                login(request,user_ob)
                messages.success(request,"Login Successfully")
                return redirect('Home')
            else:
                return render(request,'log.html',{'form':form_data})
    
class Lgout(View):
    def get(self,request):
        logout(request)
        return redirect("logv")