from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),
    path('some_view',views.some_view,name='some_view')


]