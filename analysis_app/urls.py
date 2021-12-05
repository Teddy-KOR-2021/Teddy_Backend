from django.contrib import admin
from django.urls import path
import analysis_app.views

urlpatterns = [
    path('index/', analysis_app.views.index),
    path('testdg1/', analysis_app.views.dg1),
    path('dg1data/', analysis_app.views.dg1data),
    path('testdg2/', analysis_app.views.dg2),
    path('testdg3/', analysis_app.views.dg3),
    path('dg3data/', analysis_app.views.dg3data),
    path('testdg4/', analysis_app.views.dg4),
    path('dg4data1/', analysis_app.views.dg4data1),
    path('dg4data2/', analysis_app.views.dg4data2),
    path('dg4data3/', analysis_app.views.dg4data3),
    path('dg4data4/', analysis_app.views.dg4data4),
    path('dg4data5/', analysis_app.views.dg4data5),
    path('dg4data6/', analysis_app.views.dg4data6),
    path('dg4data7/', analysis_app.views.dg4data7),
    path('testdg5/', analysis_app.views.dg5),
    path('testdg6/', analysis_app.views.dg6),
    path('dg6data/', analysis_app.views.dg6data),
]
