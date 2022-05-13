# Generated by Django 4.0.4 on 2022-05-13 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Referido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('telefone', models.CharField(max_length=200)),
                ('prioridade', models.CharField(choices=[('Neutro', 'Neutro'), ('Sim', 'Sim'), ('Não', 'Não')], default='Neutro', max_length=200)),
                ('status', models.CharField(choices=[('Iniciar', 'INICIAR'), ('Ligação 1', 'LIGACAO_1'), ('Ligação 2', 'LIGACAO_2'), ('Ligação 3', 'LIGACAO_3'), ('Mandar áudio', 'MANDA_AUDIO'), ('Áudio enviado', 'AUDIO_ENVIADO'), ('Agendado', 'AGENDADO'), ('Mandar texto', 'MANDAR_TEXTO'), ('Texto enviado', 'TEXTO_ENVIADO'), ('Não venda', 'NAO_VENDA'), ('Venda', 'VENDA')], default='Iniciar', max_length=200)),
                ('quem_indicou', models.CharField(max_length=200)),
            ],
        ),
    ]