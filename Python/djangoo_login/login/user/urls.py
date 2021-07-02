from django.urls import path
from . import views

urlpatterns =[

    path('login/',views.acc_login,name ='acc_login'),
    path('index/',views.index,name='index'),
    path('logout/',views.acc_logout,name='acc_logout'),

    path('com_list/',views.com_list,name='com_list')
]