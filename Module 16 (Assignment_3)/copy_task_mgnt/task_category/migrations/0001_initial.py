# Generated by Django 5.1.1 on 2024-11-26 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('task_model', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('task', models.ManyToManyField(to='task_model.task')),
            ],
        ),
    ]