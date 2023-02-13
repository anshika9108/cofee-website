# Generated by Django 4.1.3 on 2022-12-06 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=30)),
                ('contact', models.IntegerField(max_length=30)),
                ('password', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'student',
            },
        ),
    ]
