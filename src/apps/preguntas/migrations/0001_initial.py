# Generated by Django 3.2.7 on 2021-09-08 17:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaPregunta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreCategoria', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'categorias',
            },
        ),
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pregunta', models.CharField(max_length=250)),
                ('dificultadPregunta', models.CharField(choices=[('1', 'Fácil'), ('2', 'Media'), ('3', 'Difícil')], default='1', max_length=1)),
                ('categoriaPregunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='preguntas.categoriapregunta')),
            ],
        ),
        migrations.CreateModel(
            name='Opcion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.CharField(max_length=250)),
                ('valido', models.BooleanField(default=False)),
                ('pertenecientePregunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='preguntas.pregunta')),
            ],
        ),
    ]
