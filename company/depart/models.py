from django.db import models
from django.utils.timezone import now
from django.core.exceptions import ValidationError


class Departament(models.Model):
    '''
    Класс для описания департамента.
    '''

    name = models.TextField(
        max_length=256,
        verbose_name='Название департамента'
    )


class Employee(models.Model):
    '''
    Модель для всех работников(Директора и обычные работники).
    '''

    name = models.CharField(max_length=200, verbose_name='Имя сотрудника')
    last_name = models.CharField(
        max_length=200,
        verbose_name='Фамилия сотрудника'
    )
    position = models.CharField(max_length=256, verbose_name='Роль')
    salary = models.DecimalField(
        max_digits=9,
        decimal_places=3,
        verbose_name='Зарплата'
    )
    birth_date = models.DateField()
    depart = models.ForeignKey(
        Departament,
        on_delete=models.DO_NOTHING,
        related_name='employee',
        verbose_name='Pаботник департамента',
    )

    @property
    def get_age(self):
        if self.birth_date:
            current_age = now().date().year - self.birth_date.year
            return current_age
        return 0

    @property
    def full_name(self):
        return f'{self.name} {self.last_name}'
    

class DirectorDepart(models.Model):
    '''
    Модель для директоров департамента.
    '''

    director = models.OneToOneField(
        Employee,
        on_delete=models.DO_NOTHING,
        related_name='boss_of_depart',
        verbose_name='Директор департамента'
    )
    depart = models.OneToOneField(
        Departament,
        on_delete=models.DO_NOTHING,
        related_name='depart',
        verbose_name='Название департамента'
    )

    def clean(self):
        if self.depart != self.director.depart:
            raise ValidationError(
                {'depart': "Сотрудник может быть директором департамента, в котором он работает"}
            )
        
    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)
