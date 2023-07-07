from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
router=DefaultRouter()
router.register("prod",ProductVSet,basename="prod")
router.register("product",ProductMVset,basename="pmv")
router.register("user",UserVset,basename="us")

urlpatterns = [
     path('product',ProductView.as_view()),
     path('product/<int:id>',Specificview.as_view()),
     path('token',views.obtain_auth_token),
]+router.urls
