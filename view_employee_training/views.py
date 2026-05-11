from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from database_models.models import Employee, Contractor
from django.db.models import Q


def view_employee_training(request):

    members = Employee.objects.all().order_by('-updated_at')
    cont_members = Contractor.objects.all().order_by('-updated_at')
    context = {
        'members': members,
        'cont_members': cont_members,
    }
    return render(request, 'view_employee_training.html', context)



def emp_details(request, emp):

    details = get_object_or_404(Employee, pk=emp)

    context = {
        'details': details,
    }

    return render(request, 'emp_details.html', context)

def cont_details(request, cont):
    
    details = get_object_or_404(Contractor,pk=cont)

    context = {
        'details': details
    }
    return render(request, 'cont_details.html', context)

def search(request):
    if request.method == 'GET':
        item = request.GET.get('keyword')
        search_item = Employee.objects.filter(Q(first_name__icontains = item) | Q(last_name__icontains = item) | Q(company_ID__icontains = item))
        context = {
            'search_item': search_item,
            'item': item,
        }
        return render(request, 'searchpage.html', context)
    
def cont_search(request):
    if request.method == 'GET':
        cont_item = request.GET.get('cont_keyword')
        cont_search_item = Contractor.objects.filter(Q(first_name__icontains = cont_item) | Q(last_name__icontains = cont_item) | Q(id_number__icontains = cont_item))
        context = {
            'cont_search_item': cont_search_item,
            'cont_item': cont_item,
        }
        return render(request, 'cont_searchpage.html', context)