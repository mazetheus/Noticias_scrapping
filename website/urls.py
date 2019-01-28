from website.views import IndexTemplateView, NoticiaListView, BuscaNoticia
from django.urls import path

app_name = 'website'

urlpatterns = [
    # GET /
    path('', IndexTemplateView.as_view(), name="index"),

    # GET /Noticias
    path('Noticias/', NoticiaListView.as_view(), name="lista_noticias"),

    #Caminho para função de busca - Não está funcionando -
    path('Noticias/', BuscaNoticia.as_view(), name="busca_noticia")
]
