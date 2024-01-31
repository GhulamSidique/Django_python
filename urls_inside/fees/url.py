from django.urls import path
from django.contrib import admin
from fees import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('py_fess/', views.py_fees),
    path('py_lib_fees/', views.py_lib_fees),
]