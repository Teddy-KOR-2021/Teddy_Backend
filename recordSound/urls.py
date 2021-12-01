from django.urls import path
from recordSound import views

urlpatterns = [
    path('', views.recordSound_list, name="recordSound_list"),
    path('<int:pk>/', views.recordSound_detail, name="recordSound_detail"),
    path('create/', views.recordSound_create, name="recordSound_create"),
]
