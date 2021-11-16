from django.urls import path

from . import views

urlpatterns = [
    path('list_employees/', EmployeeList.as_view(),name='list_employees'),
    path('edit_employee/<int:pk>',EmployeeUpdate.as_view(),name='edit_employee'),
    path('new_employee/',EmployeeCreate.as_view(),name='new_employee'),#para llamar via button usando el name
    path('delete_employee/<int:pk>',EmployeeDelete.as_view(),name='delete_employee'),
]
