from django.db import models

from mptt.models import MPTTModel, TreeForeignKey


class Department(MPTTModel):
    name = models.CharField(
        max_length=255,
        verbose_name="Department Name",
    )
    parent = TreeForeignKey(
        "self",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="children",
    )

    class MPTTMeta:
        verbose_name = "Department"
        verbose_name_plural = "Departments"
        order_insertion_by = ['name']

    def __str__(self):
        return self.name


class Employee(models.Model):
    full_name = models.CharField(
        max_length=255,
        verbose_name="Employee Name",
    )
    position = models.CharField(
        max_length=255,
        verbose_name="Position",
    )
    hire_date = models.DateField(
        verbose_name="Hire Date",
    )
    salary = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Salary",
    )
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        verbose_name='Department',
        related_name='employees',
    )

    class Meta:
        verbose_name = "Employee"
        verbose_name_plural = "Employees"

    def __str__(self):
        return self.full_name

    def get_info(self):
        return f"{self.full_name} {self.position} {self.hire_date} {self.salary}"
