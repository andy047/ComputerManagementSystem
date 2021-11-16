from django.urls import path

from report import views

urlpatterns = [
    path('reports/',views.reports,name='reports'),
    path('new_report/',views.new_report,name='new_report'),
    path('edit_report/<int:id>', views.edit_report, name='edit_report'),
    path('closed_reports/', views.closed_reports, name='closed_reports'),
    path('delete_report/<int:id>',views.delete_report,name='delete_report'),
]
