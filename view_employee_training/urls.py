from django.urls import path
from . import views

urlpatterns = [
    path('view_employee_training/', views.view_employee_training, name= 'view_employee_training'),
    path('emp_details/<int:emp>/', views.emp_details, name= 'emp_details'),
    path('cont_details/<int:cont>', views.cont_details, name='cont_details'),
    path('search/', views.search, name= 'search'),
    path('cont_search/', views.cont_search, name= 'cont_search'),
]