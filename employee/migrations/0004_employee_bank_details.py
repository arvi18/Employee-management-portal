# Generated by Django 3.2.7 on 2021-10-05 13:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_employee_dept_details'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee_bank_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_acc_no', models.CharField(max_length=12, null=True)),
                ('bank_name', models.CharField(max_length=34, null=True)),
                ('pf_no', models.CharField(max_length=12, null=True)),
                ('temp_address', models.TextField(max_length=200, null=True)),
                ('per_address', models.TextField(max_length=200, null=True)),
                ('bank_details', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='bank_details', to='employee.employee')),
            ],
        ),
    ]
