from django.urls import path
from . import views

urlpatterns = [
    path('', views.allblogs, name='allblogs'),  #if nth comes after /blog/ in the url display this
    path('<int:blog_id>/', views.detail, name='detail'),    #if integer comes after /blog/ in the url display this
]