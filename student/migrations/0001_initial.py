# Generated by Django 5.1.7 on 2025-03-16 15:52

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
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('date_of_birth', models.DateField()),
                ('admitted_class', models.CharField(max_length=50)),
                ('section', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=50)),
            ],
        ),
    ]
