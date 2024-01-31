from django.contrib import admin
from django.urls import path
from course import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('Python/', views.learn),
    path('Python_lib/', views.learn_lib),
]