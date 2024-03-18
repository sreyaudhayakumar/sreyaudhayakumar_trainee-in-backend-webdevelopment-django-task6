from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('list/', views.list_items, name='list_items'),
    path('adduser/', views.adduser, name='adduser'),
]