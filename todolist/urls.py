from django.urls import path
from todolist import views

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:id>/', views.detail, name='detail')
]
