# Generated by Django 3.2 on 2024-08-14 12:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('depart', '0009_auto_20240814_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='depart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='empoyee', to='depart.departament', verbose_name='Pаботник департамента'),
        ),
    ]
