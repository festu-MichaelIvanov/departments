from django.shortcuts import render

from app.models import Department


def department_tree(request):
    root_departments = Department.objects.filter(
        parent__isnull=True,
    )
    return render(
        request,
        "departments/tree.html",
        {
            "departments": root_departments,
        },
    )
