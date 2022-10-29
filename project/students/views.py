from django.shortcuts import render
from main.models import *
from django.views.generic import DetailView


# Главная страница студента
def index(request):
    discipline_q = request.GET.get("discipline")
    disciplines = Discipline.objects.all()
    if not discipline_q:
        mark = []
    else:
        discipline = disciplines.get(pk=discipline_q)
        month = request.GET.get("date")
        if month:
            mark = Mark.objects.filter(discipline=discipline, created__month=month).order_by('created')
        else:
            mark = Mark.objects.filter()


    month_all = request.GET.get("date-all")

    if month_all:
        mark_all = Mark.objects.filter(created__month=month_all)
    else:
        mark_all = Mark.objects.filter()

    table = {
        'disciplines': disciplines,
        'marks': mark,
        'marks_all': mark_all
    }
    print(table)

    return render(request, 'students/index.html', table)
    


