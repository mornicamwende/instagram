from django.urls import path
from .import views

urlpatterns = [
    path('',views.home, name='Instagram-Home'),
    path('about/',views.about, name='Instagram-about'),

]
