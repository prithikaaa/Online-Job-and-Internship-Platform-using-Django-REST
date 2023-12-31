# Generated by Django 4.2.4 on 2023-08-10 11:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=50)),
                ('slug', models.SlugField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='static/jobs')),
                ('salary', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=200)),
                ('stock', models.IntegerField(default=50)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.category')),
            ],
        ),
    ]
