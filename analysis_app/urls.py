from django.contrib import admin
from django.urls import path
import analysis_app.views

urlpatterns = [
    path('testdg6/', analysis_app.views.dg6),
    path('dg6data/', analysis_app.views.dg6data),
]
