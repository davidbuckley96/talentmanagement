from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('article/<str:pk>/', views.article, name='article'),
    path('articles/', views.articles_list, name='articles-list'),
    path('about/', views.about, name='about'),
    path('why/', views.why_us, name='why-us')
]


