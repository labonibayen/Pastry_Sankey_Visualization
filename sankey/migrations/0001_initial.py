# Generated by Django 4.1.10 on 2023-09-04 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataPoint',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('element', models.CharField(max_length=200)),
                ('category', models.CharField(default='SOME STRING', max_length=500)),
                ('bool_val', models.IntegerField(default=0)),
                ('element_description', models.CharField(default=True, max_length=1000)),
                ('total_value', models.IntegerField(default=0)),
                ('in_sankey', models.BooleanField(default=False)),
                ('rank', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ('rank',),
            },
        ),
    ]