# Generated by Django 4.1.1 on 2022-12-09 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('track', '0003_alter_projecttask_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projecttask',
            name='status',
            field=models.CharField(choices=[('complete', 'complete'), ('canceled', 'canceled'), ('todo', 'todo')], default='todo', max_length=25),
        ),
    ]