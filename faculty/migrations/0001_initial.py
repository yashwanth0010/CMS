# Generated by Django 4.1.7 on 2023-03-23 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty_data',
            fields=[
                ('fno', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=25)),
                ('department', models.CharField(max_length=10)),
                ('subjects', models.JSONField()),
                ('students', models.JSONField()),
            ],
            options={
                'db_table': 'faculty',
                'managed': False,
            },
        ),
    ]
