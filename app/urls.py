from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('login/',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('doctors/',views.doctors,name='doctors'),
    path('doctors/<str:name>',views.doctor,name='doctor')
]
