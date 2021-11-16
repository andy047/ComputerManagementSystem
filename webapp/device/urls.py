from django.urls import path

from . import views

urlpatterns = [
    path('devices/', views.devices,name='devices'),
    path('new_device/', views.new_device, name='new_device'),
    path('new_dev_report/', views.new_dev_report, name='new_dev_report'),
    path('edit_device/<int:id>',views.edit_device,name='edit_device'),
    path('delete_device/<int:id>',views.delete_device,name='delete_device'),
]
