from django.shortcuts import render
from django.shortcuts import redirect


# Перенаправление на профиль после авторизации
def login_success(request):
    """
    Redirects users based on whether they are in the admins group
    """
    if request.user.groups.filter(name="Students").exists():
        return redirect("student_profil")
    elif request.user.groups.filter(name="Teachers").exists():
        return redirect("teacher_profil")
    else :
        return redirect("main")