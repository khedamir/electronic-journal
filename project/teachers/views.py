from django.shortcuts import render
from main.models import *
from django.contrib.auth.models import AbstractUser
from django.views.generic import DetailView
from django.views.generic.list import ListView

from .forms import MarkForm



# Главная страница преподавателя
def index(request):
    teacher = Teacher.objects.get(user=request.user.id)
    discipline_q = request.GET.get("discipline")
    disciplines = Discipline.objects.filter(teacher=teacher).all()
    if not discipline_q:
        student_group = []
        table = {
            'disciplines': disciplines,
            'student_groups': student_group,
        }
    else:
        discipline = disciplines.get(pk=discipline_q)
        student_group = StudentGroup.objects.filter(discipline=discipline)

        table = {
            'disciplines': disciplines,
            'student_groups': student_group,
            'discipline_group': discipline
        }
    return render(request, 'teachers/index.html', table)


class A():
    pass


# Журнал группы
class GroupDetailView(ListView):
    model = StudentGroup
    template_name = 'teachers/group_details.html'
    

    def get_context_data(self, **kwargs):
        context = super(GroupDetailView, self).get_context_data(**kwargs)
        context['student_group'] = StudentGroup.objects.get(id = self.kwargs['pk'])
        context['discipline_group'] = Discipline.objects.get(id=self.kwargs['pk1'])
        teacher = Teacher.objects.get(user=self.request.user.id)
        data = {'discipline': context['discipline_group'], 'teacher': teacher,  }
        context['form'] = MarkForm(data)
        print(context)
        return context

    def post(self, *args, **kwargs):
        return self.get(*args, **kwargs)
    
    def get_queryset(self, **kwargs):
        form = MarkForm(self.request.POST)
        if form.is_valid():
            form.save()
        obj = A()
        month = self.request.GET.get("date")
        student_group = StudentGroup.objects.get(id = self.kwargs['pk'])
        m  = Mark.objects.filter(student__stdgroup=student_group, created__month=month).values_list("student__name", flat=True).distinct()
        obj.dates=Mark.objects.filter(student__stdgroup=student_group, created__month=month).values_list("created", flat=True).distinct().order_by('created')
        
        group_by_value = []
        for value in m:
            stud=A()
            stud.fio=value
            stud.marks=Mark.objects.filter(student__name=value)
            stud.dmarks=[]
            for i in [i.day for i in obj.dates ]:
                dm=A()
                dm.day=i
                
                if(stud.marks.filter(created__day=i)):
                    dm.mark=stud.marks.filter(created__day=i)[0]
                stud.dmarks.append(dm)
            group_by_value.append(stud)
        obj.students=group_by_value,
        return obj
