# Generated by Django 4.1.7 on 2023-03-21 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_faculty_student_rollno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty',
            name='department',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='fno',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='student',
            name='department',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='student',
            name='rollno',
            field=models.CharField(max_length=20),
        ),
    ]
