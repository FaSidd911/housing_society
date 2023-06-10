# Generated by Django 3.2.18 on 2023-06-04 13:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SocietyList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('societyName', models.CharField(max_length=500)),
                ('regno', models.CharField(max_length=122)),
                ('address', models.TextField()),
                ('date_add_society', models.DateField()),
                ('charges_fields', models.CharField(blank=True, max_length=122, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MembersList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Member_Name', models.CharField(max_length=500)),
                ('Flat_No', models.CharField(max_length=122)),
                ('Opening_Balance', models.IntegerField()),
                ('Closing_Balance', models.IntegerField()),
                ('Electricity_Charges', models.CharField(blank=True, max_length=122, null=True)),
                ('Water_Charges', models.CharField(blank=True, max_length=122, null=True)),
                ('Maintainance_Charges', models.CharField(blank=True, max_length=122, null=True)),
                ('Municipal_Tax', models.CharField(blank=True, max_length=122, null=True)),
                ('Sinking_Fund', models.CharField(blank=True, max_length=122, null=True)),
                ('Repair_Fund', models.CharField(blank=True, max_length=122, null=True)),
                ('Service_Charges', models.CharField(blank=True, max_length=122, null=True)),
                ('date_add_member', models.DateField()),
                ('memberSocietyName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.societylist')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]