main

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pages', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_social', models.CharField(max_length=75, unique=True)),
                ('nome_fantasia', models.CharField(max_length=75, unique=True)),
                ('cnpj', models.CharField(max_length=18, unique=True)),
                ('fk_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='empresa', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Servicos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('descricao', models.CharField(max_length=150)),
                ('fk_empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='servicos', to='auth_user.empresa')),
            ],
        ),
        migrations.CreateModel(
            name='Pontos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('spent', models.IntegerField()),
                ('updated', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pontos', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LogSaida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt_saida', models.DateTimeField()),
                ('qt_saida', models.IntegerField()),
                ('fk_doador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doador_saida', to=settings.AUTH_USER_MODEL)),
                ('fk_donatario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='donatario', to=settings.AUTH_USER_MODEL)),
                ('fk_pet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pet', to='pages.pet')),
            ],
        ),
        migrations.CreateModel(
            name='LogEntrada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('raca', models.CharField(max_length=75)),
                ('sexo', models.CharField(max_length=15)),
                ('dt_entrada', models.DateTimeField()),
                ('fk_doador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doador_entrada', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cep', models.CharField(max_length=8)),
                ('cidade', models.CharField(max_length=75)),
                ('rua', models.CharField(max_length=80)),
                ('numero', models.IntegerField()),
                ('fk_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='endereco', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DefaultUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telefone', models.CharField(max_length=13, unique=True)),
                ('fk_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='defaultUser', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
