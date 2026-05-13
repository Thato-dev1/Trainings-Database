from django.shortcuts import render, redirect
from django.http import HttpResponse
from database_models.models import Employee, Contractor, TrainingModule
from django.contrib.auth.decorators import login_required



# def add_employee_training(request):
#     return render(request, 'add_employee_training.html')
@login_required   
def add_employee(request):
    if request.method == 'POST':
        company_ID = request.POST.get('company_ID')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        employee_type = request.POST.get('employee_type')

        employee, created = Employee.objects.get_or_create(
            company_ID = company_ID,
            defaults={
                'first_name': first_name,
                'last_name': last_name,
                'employee_type': employee_type,
            }
        )

        selected_modules = request.POST.getlist('training_module')

        for module in selected_modules:
            TrainingModule.objects.create(
                employee = employee,
                training_module = int(module),
                start_date = request.POST.get('start_date'),
                end_date = request.POST.get('end_date'),
                course_description = request.POST.get('course_description'),
                trainer_company_ID = request.POST.get('trainer_company_ID'),
                trainer_name = request.POST.get('trainer_name'),
                trainer_surname = request.POST.get('trainer_surname'),
                hours_of_training = request.POST.get('hours_of_training'),
                captured_by = request.user
                )
        return redirect('add_employee')
    else:
        return render(request, 'add_employee_training.html')

@login_required
def add_contractor(request):
    if request.method == 'POST':
        id_number = request.POST.get('id_number')
        company_name = request.POST.get('company_name')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        contractor, created = Contractor.objects.get_or_create(
            id_number = id_number,
            defaults={
                'company_name': company_name,
                'first_name': first_name,
                'last_name': last_name,
            }
        )

        modules = request.POST.getlist('training_module')

        for module in modules:
            TrainingModule.objects.create(
                contractor = contractor,
                training_module = int(module),
                start_date = request.POST.get('start_date'),
                end_date = request.POST.get('end_date'),
                course_description = request.POST.get('course_description'),
                trainer_company_ID = request.POST.get('trainer_company_ID'),
                trainer_name = request.POST.get('trainer_name'),
                trainer_surname = request.POST.get('trainer_surname'),
                hours_of_training = request.POST.get('hours_of_training'),
                captured_by = request.user
            )
        return redirect('add_contractor')
    else:
        return render(request, 'add_employee_training.html')

