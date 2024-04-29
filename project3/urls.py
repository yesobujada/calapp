from django.contrib import admin
from django.urls import path
from calapp import views
urlpatterns = [
    path('admin/',admin.site.urls),
    path('calapp',views.input),
    path('calculate',views.calculate),
]
