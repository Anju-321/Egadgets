from django.urls import path
from .views import *

urlpatterns = [
    path("cust",CusthomeView.as_view(),name="Home"),
    path("prod/<int:pid>",ProductDetailView.as_view(),name="pdet"),
    path("acart/<int:id>",AddCart.as_view(),name="acart"),
    path("Cartview",CartListView.as_view(),name="vcart"),
    path("delcar/<int:id>",deletecartitem,name="delcart"),
    path("Cancel/<int:id>",cancelordertitem,name="corder"),
    path("checkout/<int:cid>",CheckoutView.as_view(),name="checkout"),
    path("Order",OrderView.as_view(),name="order"),
    
]
