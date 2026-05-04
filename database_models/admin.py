from django.contrib import admin
from database_models.models import Employee, Contractor, TrainingModule

class TrainingModuleAdmin(admin.ModelAdmin):
    search_fields = ('training_module',)

admin.site.register(Employee)
admin.site.register(Contractor)
admin.site.register(TrainingModule, TrainingModuleAdmin)
