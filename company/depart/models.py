from django.db import models
from django.utils.timezone import datetime


class Director(models.Model):
    '''
    Модель для директора департамента.
    '''

    name = models.CharField(max_length=200, verbose_name='Имя начальника')
    last_name = models.CharField(max_length=200, verbose_name='Имя начальника')
    position = models.CharField(max_length=256, verbose_name='Роль')
    salary = models.DecimalField(
        max_digits=9,
        decimal_places=3,
        verbose_name='Зарплата'
    )
    birth_date = models.DateField(verbose_name='дата рождения')

    def get_age(self):
        age = datetime.date.today()-self.birth_date
        return int((age).days/365.25)
    
    @property
    def full_name(self):
        return f'{self.name} {self.last_name}'


class Departament(models.Model):
    '''
    Класс для описания департамента.
    '''

    name = models.TextField(
        max_length=256,
        verbose_name='Название департамента'
    )

    boss = models.OneToOneField(
        Director,
        on_delete=models.DO_NOTHING,
        related_name='depart',
        verbose_name='Директор департамента',
    )


class Employee(models.Model):
    '''
    Модель для директора работника.
    '''

    name = models.CharField(max_length=200, verbose_name='Имя сотрудника')
    last_name = models.CharField(max_length=200, verbose_name='Фамилия сотрудника')
    position = models.CharField(max_length=256, verbose_name='Роль')
    salary = models.DecimalField(
        max_digits=9,
        decimal_places=3,
        verbose_name='Зарплата'
    )
    birth_date = models.DateField()
    depart = models.ForeignKey(
        Departament,
        related_name='empoyee',
        verbose_name='работники департамента',
        on_delete=models.DO_NOTHING
    )

    def get_age(self):
        age = datetime.date.today()-self.birth_date
        return int((age).days/365.25)

    @property
    def full_name(self):
        return f'{self.name} {self.last_name}'
