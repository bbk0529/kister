# Generated by Django 2.2.16 on 2020-10-16 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grundwasserstand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('messdat', models.DateTimeField()),
                ('gwh', models.FloatField()),
                ('gwt', models.FloatField()),
                ('bnr', models.IntegerField()),
            ],
        ),
    ]
