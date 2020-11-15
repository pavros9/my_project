from django.urls import path
from . import views
from django.views.generic import DetailView
from .models import Article

urlpatterns = [
    path('', views.index, name='home'),
    path('projects', views.projects, name='projects'),
    path('aboutme', views.aboutme, name='aboutme'),
    path('aboutsite/', views.aboutsite, name='aboutsite'),
    path('aboutsite/<int:pk>', views.AboutSiteDetailView.as_view(), name='posts-detail'),
    path('aboutme', views.AboutMeDetailView.as_view(), name='photo-detail'),
]
