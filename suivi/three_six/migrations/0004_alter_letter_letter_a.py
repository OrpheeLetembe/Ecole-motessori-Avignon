# Generated by Django 4.0.5 on 2022-06-22 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('three_six', '0003_letter_letter_j_letter_letter_m_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='letter',
            name='letter_a',
            field=models.CharField(choices=[('Présentée', 'Présentée'), ('Entendue', 'Entendue'), ('Lue', 'Lue'), ('Ecrite', 'Ecrite')], default='', max_length=100, verbose_name='A'),
        ),
    ]
