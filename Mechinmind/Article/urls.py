from django.urls import path

from . import views

urlpatterns = [
    path('list', views.list),
    path('view/<int:id>/', views.view),
]
