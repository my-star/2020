from django.urls import path,include
from . import views

urlpatterns = [
    path('index/',views.index,name='index'),
    path('login/',views.login,name='login'),
    #path('/', views.add_emp, name='add_emp'),
    path('register/',views.register,name='register')

]