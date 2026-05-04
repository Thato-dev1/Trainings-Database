from django.urls import path
from . import views


urlpatterns = [
    # path('add_employee_training/', views.add_employee_training, name= 'add_employee_training' ),
    path('add_employee/', views.add_employee, name= 'add_employee' ),
    path('add_contractor/', views.add_contractor, name= 'add_contractor'),
]