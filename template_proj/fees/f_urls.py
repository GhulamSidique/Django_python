from django.contrib import admin
from django.urls import path
from fees import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('fees', views.fees),
]
