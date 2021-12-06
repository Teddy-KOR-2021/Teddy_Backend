from django.urls import path
from recordSound import views

urlpatterns = [
    path('', views.recordSound_list, name="recordSound_list"),
    path('<int:pk>/', views.recordSound_detail, name="recordSound_detail"),
    path('create/', views.recordSound_create, name="recordSound_create"),
    path('publish/create/', views.mqtt_text_create, name="mqtt_text_create"),
    path('publish/list/', views.mqtt_text_list, name="mqtt_text_list"),
    path('publish/', views.publish, name="publish"),
]

