from django.urls import path
from . import views

urlpatterns = [
  path('index/', views.index, name="index"),
  path('graph/', views.graph, name="graph"),
  path('alarm/',views.alarm, name="alarm"),
  path('camera/',views.camera, name="camera"),
  path('info/',views.info, name="info"),
]