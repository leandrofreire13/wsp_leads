from django.db import models

# Create your models here.


STATUS_REFERIDOS = (
    ('Iniciar', 'INICIAR'),
    ('Ligação 1', 'LIGACAO_1'),
    ('Ligação 2', 'LIGACAO_2'),
    ('Ligação 3', 'LIGACAO_3'),
    ('Mandar áudio','MANDA_AUDIO'),
    ('Áudio enviado','AUDIO_ENVIADO'),
    ('Agendado','AGENDADO'),
    ('Mandar texto','MANDAR_TEXTO'),
    ('Texto enviado','TEXTO_ENVIADO'),
    ('Não venda','NAO_VENDA'),
    ('Venda','VENDA'),
)

PRIORIDADE = (
   ('Neutro', 'Neutro'),
   ('Sim', 'Sim'),
   ('Não', 'Não')
)

ALUNO = (
   ('Sim', 'Sim'),
   ('Não', 'Não')
)
class Referido(models.Model):
    nome = models.CharField(max_length=200)
    telefone = models.CharField(max_length=200)
    prioridade = models.CharField(max_length=200, choices=PRIORIDADE, default="Neutro")
    status = models.CharField(max_length=200, choices=STATUS_REFERIDOS, default='Iniciar')
    quem_indicou = models.CharField(max_length=200)
    aluno = models.CharField(max_length=200, choices=ALUNO, default='Sim')

    def __str__(self):
        return self.nome