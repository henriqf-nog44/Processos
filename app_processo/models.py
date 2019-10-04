from django.db import models
from django.contrib.auth.models import User


class Departamento(models.Model):
    nome = models.CharField('Nome do Departamento', max_length=40)
    funcao = models.CharField('Função', max_length=50)

    def __str__(self):
        return self.nome


class Pessoa(models.Model):
    nome = models.CharField('Nome', max_length=30)
    data_de_nascimento = models.DateField('Data de nascimento', blank=True, null=True)
    cpf = models.IntegerField('CPF')

    def __str__(self):
        return self.nome


class Funcionario(Pessoa):
    matricula = models.IntegerField('Matrícula')


class Processo(models.Model):
    numero = models.IntegerField('Número')
    data_criacao = models.DateField(auto_now_add=True)
    funcionario = models.ForeignKey(Funcionario, verbose_name='Funcionário', on_delete=models.SET_NULL, null=True,
                                    blank=True)
    local = models.ForeignKey(Departamento, on_delete=models.SET_NULL, null=True, blank=True)
    interessados = models.ManyToManyField(Pessoa, related_name='interessados_processo_set')
    investigados = models.ManyToManyField(Pessoa, related_name='investigados_processo_set')

    def __str__(self):
        return str(self.numero)


class Documento(models.Model):
    numero = models.IntegerField('Número')
    titulo = models.CharField(max_length=100)
    data_criacao = models.DateField(auto_now_add=True)
    texto = models.TextField()
    processo = models.ForeignKey(Processo, on_delete=models.CASCADE, null=True)
    usuario = models.ForeignKey(Funcionario, verbose_name='Funcionário', on_delete=models.SET_NULL, null=True,
                                blank=True)

    def __str__(self):
        return self.titulo


class Portaria(Documento):
    justificativa = models.TextField()
    data_prazo = models.DateField()


class PedidoDePrazo(Documento):
    justificativa = models.TextField()
    data_prazo_anterior = models.DateField()
    data_prazo_novo = models.DateField()


class EnvioDeProcesso(Documento):
    departamento_envio = models.ForeignKey(Departamento, related_name='departamentonovo_enviodeprocesso_set',
                                           on_delete=models.SET_NULL, null=True, blank=True)
    data_envio = models.DateField()


class Tramitacao(models.Model):
    processo = models.ForeignKey(Processo, on_delete=models.CASCADE)
    departamento_anterior = models.ForeignKey(Departamento, related_name='departamentoanterior_tramitacao_set',
                                              on_delete=models.SET_NULL, null=True, blank=True)
    departamento_novo = models.ForeignKey(Departamento, related_name='departamentonovo_tramitacao_set',
                                          on_delete=models.SET_NULL, null=True, blank=True)
    data_origem = models.DateField()
    data_movimentacao = models.DateField()

    def __str__(self):
        return 'De: ' + self.departamento_anterior.nome + ' - Para: ' + self.departamento_novo.nome
