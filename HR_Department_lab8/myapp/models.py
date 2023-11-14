from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Projects(models.Model):
    ProjectNumber = models.AutoField(primary_key=True)
    ProjectName = models.TextField()
    Deadline = models.DateField()
    Funding = models.DecimalField(max_digits=12, decimal_places=2)

    def str(self):
        return self.ProjectName


class Positions(models.Model):
    PositionID = models.AutoField(primary_key=True)
    PositionName = models.TextField()
    Salary = models.DecimalField(max_digits=10, decimal_places=2)
    BonusPercentage = models.DecimalField(max_digits=5, decimal_places=2,
                                          validators=[MinValueValidator(0), MaxValueValidator(100)])

    def str(self):
        return self.PositionName


class Departments(models.Model):
    DepartmentID = models.AutoField(primary_key=True)
    DepartmentName = models.TextField()
    PhoneNumber = models.TextField()
    RoomNumber = models.PositiveIntegerField(validators=[MinValueValidator(701), MaxValueValidator(710)], unique=True)

    def str(self):
        return self.DepartmentName


class Employees(models.Model):
    EmployeeID = models.AutoField(primary_key=True)
    LastName = models.TextField()
    FirstName = models.TextField()
    MiddleName = models.TextField()
    Address = models.TextField()
    Phone = models.TextField()
    Education = models.CharField(max_length=20,
                                 choices=[('спеціальна', 'спеціальна'), ('середня', 'середня'), ('вища', 'вища')])
    DepartmentID = models.ForeignKey(Departments, on_delete=models.CASCADE)
    PositionID = models.ForeignKey(Positions, on_delete=models.CASCADE)

    def str(self):
        return f"{self.LastName}, {self.FirstName}"


class ProjectExecution(models.Model):
    ExecutionID = models.AutoField(primary_key=True)
    ProjectNumber = models.ForeignKey(Projects, on_delete=models.CASCADE)
    DepartmentID = models.ForeignKey(Departments, on_delete=models.CASCADE)
    StartDate = models.DateField()

    def str(self):
        return f"Execution ID: {self.ExecutionID}"
