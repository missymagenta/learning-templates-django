from django.urls import path
from . import views


#set the namespace
app_name = 'basicapp'

urlpatterns = [
    path('other/', views.other, name='other'),
    path('relative/', views.relative, name='relative'),
]
