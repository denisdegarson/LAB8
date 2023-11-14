from django.shortcuts import render
from .models import Projects, Positions, Departments, Employees, ProjectExecution

def my_page(request):
    projects = Projects.objects.all()
    positions = Positions.objects.all()
    departments = Departments.objects.all()
    employees = Employees.objects.all()
    project_execution = ProjectExecution.objects.all()

    context = {
        'projects': projects,
        'positions': positions,
        'departments': departments,
        'employees': employees,
        'project_execution': project_execution,
        'student_info': {
            'name': 'Карпович Денис',
            'group': 'КН-22004БСК',
        },
    }

    return render(request, 'template.html', context)
