# Generated by Django 4.2 on 2023-05-01 18:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cronograma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Atividade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horario_inicial', models.TimeField()),
                ('horario_final', models.TimeField()),
                ('atividade', models.CharField(max_length=75)),
                ('dia_da_semana', models.CharField(choices=[('SEGUNDA', 'Segunda-feira'), ('TERCA', 'Terça-feira'), ('QUARTA', 'Quarta-feira'), ('QUINTA', 'Quinta-feira'), ('SEXTA', 'Sexta-feira'), ('SABADO', 'Sábado'), ('DOMINGO', 'Domingo')], max_length=10)),
                ('cronograma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='atividades', to='cronograma.cronograma')),
            ],
        ),
    ]