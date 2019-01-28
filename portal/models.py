from django.db import models


class Noticia(models.Model):

    titulo = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    def __str__(self):
       return self.titulo

    objects = models.Manager()