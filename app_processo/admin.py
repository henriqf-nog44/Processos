from django.contrib import admin

from .models import Departamento, Pessoa, Documento, Processo, Portaria, PedidoDePrazo, EnvioDeProcesso, Tramitacao, Funcionario

admin.site.register(Departamento)
admin.site.register(Pessoa)
admin.site.register(Documento)
admin.site.register(Processo)
admin.site.register(Portaria)
admin.site.register(PedidoDePrazo)
admin.site.register(EnvioDeProcesso)
admin.site.register(Tramitacao)
admin.site.register(Funcionario)
