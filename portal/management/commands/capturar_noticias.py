from django.core.management.base import BaseCommand
from django.utils import timezone
from portal.models import Noticia
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

class Command(BaseCommand):
    help = 'Captura as notícias dos portais e salva no banco de dados'

    def handle(self, *args, **options):

        page = "https://www.tecmundo.com.br"
        uClient = uReq(page)
        page_html = uClient.read()
        uClient.close()
        page_soup = soup(page_html, "html.parser")

        noticias = page_soup.findAll("div", {"class": "nzn-main nzn-main-model3"})

        nova = noticias[0]

        for nova in noticias:
            nova = Noticia(
            	titulo = nova.a["title"]
            	)
            nova.save()

        print("Captura realizada com sucesso!")
