from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('list/', views.list),
    path('view/<int:id>/', views.view),
    path('getCategories/', views.geCategories),
    path('getSubCategories/', views.getSubCategories),
    path('getArticlesBySubCategories/<int:id>', views.getArticlesBySubCategories)
]
