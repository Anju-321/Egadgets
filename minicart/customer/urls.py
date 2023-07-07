from django.urls import path,include
from .views import *



urlpatterns = [
    path("regn",Regview.as_view(),name='reg'),
    path("lgout",Lgout.as_view(),name='logout'),

]