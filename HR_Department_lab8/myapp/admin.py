from django.contrib import admin
from .models import Projects, Positions, Departments, Employees, ProjectExecution

admin.site.register(Projects)
admin.site.register(Positions)
admin.site.register(Departments)
admin.site.register(Employees)
admin.site.register(ProjectExecution)

