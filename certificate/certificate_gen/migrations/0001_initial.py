# Generated by Django 4.0.5 on 2022-06-13 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=100, unique=True)),
                ('event_start_date', models.DateField(blank=True, max_length=15, null=True)),
                ('event_end_date', models.DateField(blank=True, max_length=15, null=True)),
                ('organizer', models.CharField(blank=True, max_length=15, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Players',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=150, null=True)),
                ('Registration_number', models.CharField(blank=True, max_length=150, null=True, unique=True)),
                ('Category', models.CharField(blank=True, max_length=150, null=True)),
                ('Year_of_study', models.CharField(blank=True, max_length=30, null=True)),
                ('Course', models.CharField(blank=True, max_length=100, null=True)),
                ('institution', models.CharField(blank=True, max_length=100, null=True)),
                ('department', models.CharField(blank=True, max_length=100, null=True)),
                ('location', models.CharField(blank=True, max_length=15, null=True)),
                ('event_name', models.CharField(blank=True, default='None', max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Signs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Signatories_name', models.CharField(blank=True, max_length=100, null=True)),
                ('digital_Signatures', models.FileField(blank=True, max_length=15, null=True, upload_to='')),
                ('event_name', models.CharField(max_length=100)),
            ],
        ),
    ]