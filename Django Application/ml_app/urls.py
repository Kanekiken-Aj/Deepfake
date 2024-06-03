from django.contrib import admin
from django.urls import path
from . import views

app_name = 'ml_app'
handler404 = views.handler404

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('predict/', views.predict_page, name='predict'),
    path('cuda_full/', views.cuda_full, name='cuda_full'),
]
