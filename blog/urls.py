from django.urls import path
from . import views


urlpatterns = [
    path ('' , views.home, name='home'),
    path ('about/' , views.about, name='about'),
    path ('hobbies/' , views.hobbies, name ='hobbies'),
    path ('post_list/',views.post_list, name='post_list'),
    path ('posts/new/', views.post_create, name='post_create'),
    path('signup/', views.signup, name='signup'),
   
    
]