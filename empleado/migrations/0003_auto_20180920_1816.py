# Generated by Django 2.1 on 2018-09-20 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleado', '0002_auto_20180920_1813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='domicilio',
            field=models.CharField(max_length=300, null=True),
        ),
    ]