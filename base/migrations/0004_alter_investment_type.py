# Generated by Django 4.2 on 2023-05-03 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_investment_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investment',
            name='type',
            field=models.CharField(choices=[('C', 'Compra'), ('V', 'Venda')], default='C', max_length=1, verbose_name='Tipo'),
        ),
    ]