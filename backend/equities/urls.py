from django.urls import path
from . import views


urlpatterns = [
    path('csv', views.get_csv_file),
]
