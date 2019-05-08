from django.contrib import admin
from django.urls import path

from vote import views

urlpatterns = [
    path('', views.show_subjects),
    path('captcha/', views.get_captcha),
    path('teachers/', views.show_teachers),
    path('prise/', views.praise_or_criticize),
    path('criticize/', views.praise_or_criticize),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('admin/', admin.site.urls),
]