from django.core.management.base import BaseCommand

from myapp.models import Projects, Positions, Departments, Employees, ProjectExecution


class Command(BaseCommand):
    help = 'Populate Projects, Positions, Departments, Employees, and ProjectExecution tables with data'

    def handle(self, *args, **options):
        # Заполняем Projects
        projects_data = [
            {'ProjectName': 'Проект1', 'Deadline': '2023-12-31', 'Funding': 10000.00},
            {'ProjectName': 'Проект2', 'Deadline': '2023-11-30', 'Funding': 15000.00},
            {'ProjectName': 'Проект3', 'Deadline': '2023-10-31', 'Funding': 12000.00},
            {'ProjectName': 'Проект4', 'Deadline': '2023-09-30', 'Funding': 18000.00},
            {'ProjectName': 'Проект5', 'Deadline': '2023-08-31', 'Funding': 9000.00},
            {'ProjectName': 'Проект6', 'Deadline': '2023-07-31', 'Funding': 15000.00},
            {'ProjectName': 'Проект7', 'Deadline': '2023-06-30', 'Funding': 12000.00},
            {'ProjectName': 'Проект8', 'Deadline': '2023-05-31', 'Funding': 20000.00},

        ]

        for data in projects_data:
            project = Projects(**data)
            project.save()

        # Заполняем Positions
        positions_data = [
            {'PositionName': 'Інженер', 'Salary': 50000.00, 'BonusPercentage': 5.0},
            {'PositionName': 'Редактор', 'Salary': 45000.00, 'BonusPercentage': 4.0},
            {'PositionName': 'Програміст', 'Salary': 55000.00, 'BonusPercentage': 6.0},
        ]

        for data in positions_data:
            position = Positions(**data)
            position.save()

        # Заполняем Departments
        departments_data = [
            {'DepartmentName': 'IT', 'PhoneNumber': '(123) 456-7890', 'RoomNumber': 701},
            {'DepartmentName': 'Design', 'PhoneNumber': '(234) 567-8901', 'RoomNumber': 702},
            {'DepartmentName': 'HR', 'PhoneNumber': '(345) 678-9012', 'RoomNumber': 703},
        ]

        for data in departments_data:
            department = Departments(**data)
            department.save()

        # Заполняем Employees
        employees_data = [
            {'LastName': 'Прізвище1', 'FirstName': 'Імя1', 'MiddleName': 'По батькові1', 'Address': 'Адреса1',
             'Phone': '(123) 456-7890', 'Education': 'спеціальна',
             'DepartmentID': Departments.objects.order_by('?').first(),
             'PositionID': Positions.objects.order_by('?').first()},
            {'LastName': 'Прізвище2', 'FirstName': 'Імя2', 'MiddleName': 'По батькові2', 'Address': 'Адреса2',
             'Phone': '(234) 567-8901', 'Education': 'вища', 'DepartmentID': Departments.objects.order_by('?').first(),
             'PositionID': Positions.objects.order_by('?').first()},
            {'LastName': 'Прізвище4', 'FirstName': 'Імя4', 'MiddleName': 'По батькові4', 'Address': 'Адреса4',
             'Phone': '(456) 789-0123', 'Education': 'вища', 'DepartmentID': Departments.objects.order_by('?').first(),
             'PositionID': Positions.objects.order_by('?').first()},
            {'LastName': 'Прізвище5', 'FirstName': 'Імя5', 'MiddleName': 'По батькові5', 'Address': 'Адреса5',
             'Phone': '(567) 890-1234', 'Education': 'середня',
             'DepartmentID': Departments.objects.order_by('?').first(),
             'PositionID': Positions.objects.order_by('?').first()},
            {'LastName': 'Прізвище6', 'FirstName': 'Імя6', 'MiddleName': 'По батькові6', 'Address': 'Адреса6',
             'Phone': '(678) 901-2345', 'Education': 'спеціальна',
             'DepartmentID': Departments.objects.order_by('?').first(),
             'PositionID': Positions.objects.order_by('?').first()},
            {'LastName': 'Прізвище7', 'FirstName': 'Імя7', 'MiddleName': 'По батькові7', 'Address': 'Адреса7',
             'Phone': '(789) 012-3456', 'Education': 'вища', 'DepartmentID': Departments.objects.order_by('?').first(),
             'PositionID': Positions.objects.order_by('?').first()},
            {'LastName': 'Прізвище8', 'FirstName': 'Імя8', 'MiddleName': 'По батькові8', 'Address': 'Адреса8',
             'Phone': '(890) 123-4567', 'Education': 'спеціальна',
             'DepartmentID': Departments.objects.order_by('?').first(),
             'PositionID': Positions.objects.order_by('?').first()},
            {'LastName': 'Прізвище9', 'FirstName': 'Імя9', 'MiddleName': 'По батькові9', 'Address': 'Адреса9',
             'Phone': '(901) 234-5678', 'Education': 'середня',
             'DepartmentID': Departments.objects.order_by('?').first(),
             'PositionID': Positions.objects.order_by('?').first()},
            {'LastName': 'Прізвище10', 'FirstName': 'Імя10', 'MiddleName': 'По батькові10', 'Address': 'Адреса10',
             'Phone': '(012) 345-6789', 'Education': 'спеціальна',
             'DepartmentID': Departments.objects.order_by('?').first(),
             'PositionID': Positions.objects.order_by('?').first()},
            {'LastName': 'Прізвище11', 'FirstName': 'Імя11', 'MiddleName': 'По батькові11', 'Address': 'Адреса11',
             'Phone': '(123) 456-7890', 'Education': 'вища', 'DepartmentID': Departments.objects.order_by('?').first(),
             'PositionID': Positions.objects.order_by('?').first()},
            {'LastName': 'Прізвище12', 'FirstName': 'Імя12', 'MiddleName': 'По батькові12', 'Address': 'Адреса12',
             'Phone': '(234) 567-8901', 'Education': 'середня',
             'DepartmentID': Departments.objects.order_by('?').first(),
             'PositionID': Positions.objects.order_by('?').first()},
            {'LastName': 'Прізвище13', 'FirstName': 'Імя13', 'MiddleName': 'По батькові13', 'Address': 'Адреса13',
             'Phone': '(345) 678-9012', 'Education': 'спеціальна',
             'DepartmentID': Departments.objects.order_by('?').first(),
             'PositionID': Positions.objects.order_by('?').first()},
            {'LastName': 'Прізвище14', 'FirstName': 'Імя14', 'MiddleName': 'По батькові14', 'Address': 'Адреса14',
             'Phone': '(456) 789-0123', 'Education': 'вища', 'DepartmentID': Departments.objects.order_by('?').first(),
             'PositionID': Positions.objects.order_by('?').first()},
            {'LastName': 'Прізвище15', 'FirstName': 'Імя15', 'MiddleName': 'По батькові15', 'Address': 'Адреса15',
             'Phone': '(567) 890-1234', 'Education': 'середня',
             'DepartmentID': Departments.objects.order_by('?').first(),
             'PositionID': Positions.objects.order_by('?').first()},
            {'LastName': 'Прізвище16', 'FirstName': 'Імя16', 'MiddleName': 'По батькові16', 'Address': 'Адреса16',
             'Phone': '(678) 901-2345', 'Education': 'спеціальна',
             'DepartmentID': Departments.objects.order_by('?').first(),
             'PositionID': Positions.objects.order_by('?').first()},
            {'LastName': 'Прізвище17', 'FirstName': 'Імя17', 'MiddleName': 'По батькові17', 'Address': 'Адреса17',
             'Phone': '(789) 012-3456', 'Education': 'вища', 'DepartmentID': Departments.objects.order_by('?').first(),
             'PositionID': Positions.objects.order_by('?').first()},

        ]

        for data in employees_data:
            employee = Employees(**data)
            employee.save()

        # Заполняем ProjectExecution
        project_execution_data = [
            {'ProjectNumber': Projects.objects.order_by('?').first(),
             'DepartmentID': Departments.objects.order_by('?').first(), 'StartDate': '2023-09-25'},
            {'ProjectNumber': Projects.objects.order_by('?').first(),
             'DepartmentID': Departments.objects.order_by('?').first(), 'StartDate': '2023-08-05'},
            {'ProjectNumber': Projects.objects.order_by('?').first(),
             'DepartmentID': Departments.objects.order_by('?').first(), 'StartDate': '2023-07-10'},
            {'ProjectNumber': Projects.objects.order_by('?').first(),
             'DepartmentID': Departments.objects.order_by('?').first(), 'StartDate': '2023-06-20'},
            {'ProjectNumber': Projects.objects.order_by('?').first(),
             'DepartmentID': Departments.objects.order_by('?').first(), 'StartDate': '2023-05-01'},
            {'ProjectNumber': Projects.objects.order_by('?').first(),
             'DepartmentID': Departments.objects.order_by('?').first(), 'StartDate': '2023-04-15'},
            {'ProjectNumber': Projects.objects.order_by('?').first(),
             'DepartmentID': Departments.objects.order_by('?').first(), 'StartDate': '2023-03-25'},
            {'ProjectNumber': Projects.objects.order_by('?').first(),
             'DepartmentID': Departments.objects.order_by('?').first(), 'StartDate': '2023-10-25'},
        ]

        for data in project_execution_data:
            project_execution = ProjectExecution(**data)
            project_execution.save()

        self.stdout.write(self.style.SUCCESS(
            'Successfully filled Projects, Positions, Departments, Employees, and ProjectExecution tables'))
