# Generated by Django 3.2 on 2024-08-13 19:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('depart', '0007_delete_departemp'),
    ]

    operations = [
        migrations.CreateModel(
            name='DepartEmp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('depart', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='depart.departament')),
                ('director', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='depart.director')),
                ('epmloyee', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='depart.employee')),
            ],
        ),
    ]
