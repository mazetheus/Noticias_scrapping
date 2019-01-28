from django.urls import reverse_lazy
from django. shortcuts import render
from django.views.generic import TemplateView, ListView
from portal.models import Noticia

# PÁGINA PRINCIPAL
# ----------------------------------------------

class IndexTemplateView(TemplateView):
    template_name = "website/index.html"


# LISTA DE NOTÍCIAS
# ----------------------------------------------

class NoticiaListView(ListView):
    template_name = "website/lista.html"
    model = Noticia
    context_object_name = "noticias"


# BUSCA DE NOTÍCIAS
# ----------------------------------------------
'''
Não está funcionando. O objetivo seria trazer o trecho do título que usuário
está pesquisando, criar uma QuerySet com os resultados que possuissem a string
e imprimir no mesmo template "lista"

def buscar_titulo(trecho):
   resultados = Noticia.objects.filter(titulo__contains=trecho)

'''
class BuscaNoticia(ListView):
	template_name = "website/lista.html" 
	model = Noticia
	def busca_noticia(request):
		resultados = Noticia.objects.filter(titulo__contains=request)