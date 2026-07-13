from django.db import models
from registrations.models import User

class Employee(models.Model):
    
    emp_type = (
        (0, 'Hourly'),
        (1, 'Salaried'),
    )

    company_ID = models.CharField(unique=True, max_length=7)
    first_name = models.CharField(max_length= 50)
    last_name = models.CharField(max_length= 50)
    employee_type = models.IntegerField(choices=emp_type)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)

    def __str__(self):
        return self.first_name +' '+ self.last_name
    
class Contractor(models.Model):
    id_number = models.CharField(max_length=13, unique=True)
    company_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length= 50)
    last_name = models.CharField(max_length= 50)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at= models.DateTimeField(auto_now= True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
    
class TrainingModule(models.Model):
    training_module_tuple= (
        (0, 'Induction Training'),
        (1, '5 S Workshop'),
        (2, 'FPS Training'),
        (3, '5 Whys Training'),
        (4, 'Waste Elimination'),
        (5, 'Kaizen Training'),
        (6, 'Metal Finish Training'),
        (7, 'SPII Training'),
        (8, 'Leadership Training'),
        (9, 'SPC CHarts Training'),
        (10, 'PMHV & Safety Training'),
    )
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True, blank=True, related_name='trainings')
    contractor = models.ForeignKey(Contractor, on_delete=models.CASCADE, null=True, blank=True, related_name='contractor_trainings')
    training_module = models.IntegerField(choices= training_module_tuple)
    start_date = models.DateField()
    end_date = models.DateField()
    trainer_company_ID = models.CharField(max_length= 7)
    trainer_name = models.CharField(max_length= 50)
    trainer_surname = models.CharField(max_length= 50)
    hours_of_training = models.IntegerField()
    captured_by = models.ForeignKey(User, on_delete= models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # let the User model be a foriegnkey of this model for the capture_by table feild

    def __str__(self):
        if self.employee:
            name = f"{self.employee.first_name} {self.employee.last_name}"
        elif self.contractor:
            name = f"{self.contractor.first_name} {self.contractor.first_name}"
        else:
            name = "Unknown Entity"
        
        return f"{name} - {self.get_training_module_display()}"
    

