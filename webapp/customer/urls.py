from django.urls import path

from customer import views

urlpatterns = [
    path('customers/',views.customers,name='customers'),
    path('new_customer/', views.new_customer, name='new_customer'),
    path('new_cust_report/', views.new_cust_report, name='new_cust_report'),
    path('edit_customer/<int:id>',views.edit_customer,name='edit_customer'),
    path('delete_customer<int:id>',views.delete_customer,name='delete_customer'),
]
