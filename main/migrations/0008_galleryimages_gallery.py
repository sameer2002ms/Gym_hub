# Generated by Django 4.2.6 on 2024-02-24 05:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_gallery_galleryimages'),
    ]

    operations = [
        migrations.AddField(
            model_name='galleryimages',
            name='gallery',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.gallery'),
        ),
    ]