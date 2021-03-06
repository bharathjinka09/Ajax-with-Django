# Generated by Django 3.1.5 on 2021-01-24 10:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('emp_app', '0002_delete_abc'),
    ]

    operations = [
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=20)),
                ('office', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emp_app.office')),
            ],
        ),
    ]
