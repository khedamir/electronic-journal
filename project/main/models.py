from django.db import models

# Create your models here.

from django.conf import settings

   

class StudentGroup(models.Model):
    groupname = models.CharField("Группа", max_length=15)

    def __str__(self):
        return self.groupname


class Student(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,  on_delete=models.CASCADE, limit_choices_to={'groups__name': 'Students'})
    name = models.CharField("ФИО", max_length=45)
    birth_date = models.DateField(null=True, blank=True)
    stdgroup = models.ForeignKey(StudentGroup , on_delete=models.DO_NOTHING, db_column="Группа студента")

    def __str__(self):
        return self.name


class Teacher(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,  on_delete=models.CASCADE, limit_choices_to={'groups__name': 'Teachers'})
    name = models.CharField("ФИО", max_length=45)
    birth_date = models.DateField(null=True, blank=True)
    # discgroups = models.ForeignKey(StudentGroup, on_delete=models.DO_NOTHING, db_column="Группы")

    def __str__(self):
        return self.name


class Discipline(models.Model):
    title = models.CharField(max_length=100)
    teacher = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING, db_column="Преподаватель данной дисциплины")
    group = models.ForeignKey(StudentGroup, on_delete=models.DO_NOTHING, db_column="Группа")

    def __str__(self):
        return self.title


class Lesson(models.Model):
    group = models.ForeignKey(StudentGroup, on_delete=models.DO_NOTHING, db_column="Группа")
    discipline = models.ForeignKey(Discipline, on_delete=models.DO_NOTHING, db_column="Дисциплина")
    teacher = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING, db_column="Преподаватель")


class Mark(models.Model):
    points = models.IntegerField('оценка')
    created = models.DateField('дата')
    discipline = models.ForeignKey(Discipline, on_delete=models.DO_NOTHING, db_column="Дисциплина")
    teacher = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING, db_column="Преподаватель")
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING, db_column="Студент")
