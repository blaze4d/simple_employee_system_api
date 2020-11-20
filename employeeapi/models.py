from django.db import models

class Employee(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    date_employed = models.DateField()
    salary_level = models.IntegerField()
    department = models.CharField(max_length=100)
    last_promotion_date = models.DateField(null=True)

    def __str__(self):
        return self.first_name + " " + self.last_name

class EmployeeArchive(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    date_employed = models.DateField()
    salary_level = models.IntegerField()
    department = models.CharField(max_length=100)
    last_promotion_date = models.DateField(null=True)
    archive_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name + " " + self.last_name

