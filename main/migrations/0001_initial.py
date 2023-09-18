# Generated by Django 3.2.18 on 2023-09-10 18:34

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
                ('ctsno', models.CharField(max_length=122)),
                ('panno', models.CharField(max_length=122)),
                ('gstno', models.CharField(max_length=122)),
                ('address', models.TextField()),
                ('status', models.CharField(default='Active', max_length=122)),
                ('date_add_society', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MembersList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Member_Name', models.CharField(max_length=500)),
                ('Flat_No', models.CharField(max_length=122)),
                ('building', models.CharField(max_length=122)),
                ('wing', models.CharField(max_length=122)),
                ('Contact_Number', models.CharField(max_length=122)),
                ('Balance', models.CharField(max_length=122)),
                ('PAN_Number', models.CharField(max_length=122)),
                ('Aadhar_Number', models.CharField(max_length=122)),
                ('date_add_member', models.DateField()),
                ('memberSocietyName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.societylist')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MemberChargesList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Water_Charges', models.CharField(max_length=122)),
                ('Municipal_Tax', models.CharField(max_length=122)),
                ('Maintainance_Charges', models.CharField(max_length=122)),
                ('Interest_from_Bank_Savings_Account', models.CharField(max_length=122)),
                ('Membership_Subscription_Charges', models.CharField(max_length=122)),
                ('Audit_Fees', models.CharField(max_length=122)),
                ('Staff_Welfare', models.CharField(max_length=122)),
                ('Accounting_Charges', models.CharField(max_length=122)),
                ('Postage_Courier_Charges', models.CharField(max_length=122)),
                ('Repair_Maintainence_Electrical', models.CharField(max_length=122)),
                ('Depreciation', models.CharField(max_length=122)),
                ('Meeting_Expenses', models.CharField(max_length=122)),
                ('Telephone_Charges', models.CharField(max_length=122)),
                ('Electricity_Charges', models.CharField(max_length=122)),
                ('Security_Charges', models.CharField(max_length=122)),
                ('Printing_Stationary', models.CharField(max_length=122)),
                ('Repair_Maintainence', models.CharField(max_length=122)),
                ('Conveyance', models.CharField(max_length=122)),
                ('Gardening_Expenses', models.CharField(max_length=122)),
                ('Bank_Charges', models.CharField(max_length=122)),
                ('Plumbing_Expenses', models.CharField(max_length=122)),
                ('Salary_to_Staff', models.CharField(max_length=122)),
                ('Service_Charges', models.CharField(max_length=122)),
                ('Sinking_Funds', models.CharField(max_length=122)),
                ('Repair_Funds', models.CharField(max_length=122)),
                ('Parking_Charges', models.CharField(max_length=122)),
                ('Property_Tax', models.CharField(max_length=122)),
                ('Miscellaneous_Charges', models.CharField(max_length=122)),
                ('Water_Charges_Paid', models.CharField(max_length=122)),
                ('chargesMemberName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.memberslist')),
                ('chargesSocietyName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.societylist')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DefaultChargesList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Water_Charges', models.CharField(max_length=122)),
                ('Municipal_Tax', models.CharField(max_length=122)),
                ('Maintainance_Charges', models.CharField(max_length=122)),
                ('Interest_from_Bank_Savings_Account', models.CharField(max_length=122)),
                ('Membership_Subscription_Charges', models.CharField(max_length=122)),
                ('Audit_Fees', models.CharField(max_length=122)),
                ('Staff_Welfare', models.CharField(max_length=122)),
                ('Accounting_Charges', models.CharField(max_length=122)),
                ('Postage_Courier_Charges', models.CharField(max_length=122)),
                ('Repair_Maintainence_Electrical', models.CharField(max_length=122)),
                ('Depreciation', models.CharField(max_length=122)),
                ('Meeting_Expenses', models.CharField(max_length=122)),
                ('Telephone_Charges', models.CharField(max_length=122)),
                ('Electricity_Charges', models.CharField(max_length=122)),
                ('Security_Charges', models.CharField(max_length=122)),
                ('Printing_Stationary', models.CharField(max_length=122)),
                ('Repair_Maintainence', models.CharField(max_length=122)),
                ('Conveyance', models.CharField(max_length=122)),
                ('Gardening_Expenses', models.CharField(max_length=122)),
                ('Bank_Charges', models.CharField(max_length=122)),
                ('Plumbing_Expenses', models.CharField(max_length=122)),
                ('Salary_to_Staff', models.CharField(max_length=122)),
                ('Service_Charges', models.CharField(max_length=122)),
                ('Sinking_Funds', models.CharField(max_length=122)),
                ('Repair_Funds', models.CharField(max_length=122)),
                ('Parking_Charges', models.CharField(max_length=122)),
                ('Property_Tax', models.CharField(max_length=122)),
                ('Miscellaneous_Charges', models.CharField(max_length=122)),
                ('Water_Charges_Paid', models.CharField(max_length=122)),
                ('chargesSocietyName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.societylist')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
