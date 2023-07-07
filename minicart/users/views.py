from django.db.models.query import QuerySet
from django.shortcuts import render,redirect
from typing import Any,Dict
from django.views.generic import View,TemplateView,ListView,DetailView
from store.models import Product
from .models import Cart,Order
from django.contrib import messages
from django.db.models import Sum
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache

# Create your views here.
# class CusthomeView(TemplateView):
#     template_name='cust-home.html'
    
    # def get_context_data(self, **kwargs):
    #     context=super().get_context_data(**kwargs)
    #     context['data']=Product.objects.all()
    #     return context

def signin_required(fn):
    def inner(request,*args,**kwargs):
        if request.user.is_authenticated:
            return fn(request,*args,**kwargs)
        else:
            messages.error(request,'Please Login First!!!')
            return redirect('logv')
    return inner
dec=[signin_required,never_cache]

# list view
@method_decorator(dec,name='dispatch')
class CusthomeView(ListView):
    template_name="cust-home.html"
    model=Product
    context_object_name="data"

@method_decorator(dec,name='dispatch')
class ProductDetailView(DetailView):
    template_name="product-details.html"
    model=Product
    context_object_name="product"
    pk_url_kwarg="pid"
    
@method_decorator(dec,name='dispatch')    
class AddCart(View):
    def get(self,request,*args,**kwargs):
        prod=Product.objects.get(id=kwargs.get("id"))
        user=request.user
        Cart.objects.create(product=prod,user=user)
        messages.success(request,'Product added to cart!!')
        return redirect("Home")

@method_decorator(dec,name='dispatch')
class CartListView(ListView):
    template_name='cart-list.html'
    model=Cart
    context_object_name="cartitem"

    
    def get_queryset(self):
        cart=Cart.objects.filter(user=self.request.user,status='cart')
        total=Cart.objects.filter(user=self.request.user).aggregate(tot=Sum("product__price"))
        return {'item':cart,'total':total}
    

# class DeleteCart(View):
#     def get(self,request,*args,**kwargs):
#         id=kwargs.get("mid")
#         car=Cart.objects.get(id=id)
#         car.delete()
#         return redirect("vcart")
dec
def deletecartitem(request,id):
    cart=Cart.objects.get(id=id)
    cart.delete()
    messages.error(request,"cart item removed")
    return redirect("vcart")



@method_decorator(dec,name='dispatch')   
class CheckoutView(View):
    def get(self,request,*args,**kwargs):
        return render(request,'checkout.html')
    def post(self,request,*args,**kwargs):
        id=kwargs.get("cid")
        cart=Cart.objects.get(id=id)
        prod=cart.product
        user=request.user
        address=request.POST.get("address")
        phone=request.POST.get("phone")
        Order.objects.create(product=prod,user=user,address=address,phone=phone)
        cart.status='Order Placed'
        cart.save()
        messages.success(request,"Order Placed Successfully")
        return redirect("Home")

@method_decorator(dec,name='dispatch')    
class OrderView(ListView):
    template_name='orders.html'
    model=Order
    context_object_name="orderitem"
    
    def get_queryset(self):
        order=Order.objects.filter(user=self.request.user)    
        return {'order':order}

dec    
def cancelordertitem(request,id):
    item=Order.objects.get(id=id)
    item.status='cancel'
    item.save()
    messages.error(request,"Order Cancelled")
    return redirect("order")
