from django.urls import path
from . import views

urlpatterns = [
    path('', views.calculate_signals, name='calculate_signals'),
    path('export/', views.export_numbers, name='export_numbers'),
    path('import/', views.import_numbers, name='import_numbers'),
]
