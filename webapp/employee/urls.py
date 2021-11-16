from django.urls import path

from . import views

urlpatterns = [
    path('list_employees/', views.list_employees,name='list_employees'),
    path('edit_employee/<int:id>',views.edit_employee,name='edit_employee'),
    path('new_employee/',views.new_employee,name='new_employee'),#para llamar via button usando el name
    path('delete_employee/<int:id>',views.delete_employee,name='delete_employee'),
]
