from django.contrib import admin
from evento_trabalho1.models import PessoaFisica, PessoaJuridica, Autor, Evento, EventoCientifico, ArtigoCientifico

admin.site.register(PessoaFisica)
admin.site.register(PessoaJuridica)
admin.site.register(Autor)
admin.site.register(Evento)
admin.site.register(EventoCientifico)
admin.site.register(ArtigoCientifico)
# Register your models here.
