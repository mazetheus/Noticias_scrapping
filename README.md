# Desafio: RCTech - jan.2019

Por Matheus da Silva Azevedo [omatheusazevedo@gmail.com]

## Para Instalar

Para instalar as dependências do projeto, executar:

```bash
pip install -r requirements.txt
```

Para criar as _Migrations_:

```bash
python manage.py makemigrations
```

Para efetivar as _Migrations_ no banco de dados:

```bash
python manage.py migrate
```

Para alimentar o banco de dados com as notícias dos portais

```bash
python manage.py capturar_noticias
```

## Para Executar

Para executar o Servidor de testes do Django, execute:

```bash
python manage.py runserver
```

## Busca

A caixa de busca não está implementada corretamente, porém a função em si está funcionando.

Para buscar pelo shell pode-se utilizar:
```bash
python manage.py shell
from portal.models import Noticia
Noticia.objects.filter(titulo__contains="trecho")
```
Onde "trecho" é uma parte do título da notícia.