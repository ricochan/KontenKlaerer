# Generated by Django 4.2.7 on 2023-11-26 04:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_category_ignore'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.category'),
        ),
    ]
