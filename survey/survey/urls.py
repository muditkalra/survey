from django.contrib import admin
from django.urls import path,include
from details import views
from rest_framework.routers import DefaultRouter



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',views.societyAPI.as_view(),name='apiview'),
    path('api/<int:pk>/',views.societyAPI.as_view(),name='apiview'),

]
