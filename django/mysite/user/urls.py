from django.urls import path,include
from .views import *

urlpatterns = [

    path('', IndexView.as_view(), name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/',LogoutView.as_view(),name ='logout'),
    path('home/', HomeView.as_view(),name = 'home'),

]