# Generated by Django 3.1.3 on 2020-11-19 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employeeapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeArchive',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=60)),
                ('last_name', models.CharField(max_length=60)),
                ('date_employed', models.DateField()),
                ('salary_level', models.IntegerField()),
                ('department', models.CharField(max_length=100)),
                ('last_promotion_date', models.DateField(null=True)),
                ('archive_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
