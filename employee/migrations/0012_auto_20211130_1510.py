# Generated by Django 3.2.7 on 2021-11-30 09:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0011_auto_20211128_0009'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee_leaves',
            name='leaves_details',
        ),
        migrations.AddField(
            model_name='employee_leaves',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='employee_leaves_details', to='employee.employee'),
        ),
    ]
