from django.contrib import admin
from django.urls import path
from . import views
app_name = 'movieapp'
urlpatterns = [

    path('',views.index,name='index'),
    path('movie/<int:mid>/',views.fun,name='fun'),
    path('add/',views.addmovie,name='addmovie'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete, name='delete')
]