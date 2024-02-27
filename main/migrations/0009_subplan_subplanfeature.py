# Generated by Django 4.2.6 on 2024-02-24 08:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_galleryimages_gallery'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='SubPlanFeature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('subplan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.subplan')),
            ],
        ),
    ]