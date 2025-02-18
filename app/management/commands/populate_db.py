import random

from django.core.management.base import BaseCommand
from faker import Faker

from app.models import Department, Employee


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        fake = Faker()
        root_department = Department.objects.create(name='Root Department')

        departments = {1: [root_department]}

        for level in range(2, 6):
            departments[level] = []
            for i in range(1, 6):
                parent_department = random.choice(departments[level - 1])
                department_name = f"Department L{level}-{i}"
                department = Department.objects.create(name=department_name, parent=parent_department)
                departments[level].append(department)

        root_department.refresh_from_db()
        Department.objects.rebuild()

        employees = []
        for _ in range(50000):
            employee = Employee(
                full_name=fake.name(),
                position=fake.job(),
                hire_date=fake.date_between(start_date='-10y', end_date='today'),
                salary=random.uniform(30000, 150000),
                department=random.choice([dept for sublist in departments.values() for dept in sublist])
            )
            employees.append(employee)
        Employee.objects.bulk_create(employees)

        self.stdout.write(self.style.SUCCESS('Database populated!'))
