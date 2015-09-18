# coding=utf-8
from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    """
    Agrega un Token generado automaticamente a cada usuario
    """
    if created:
        Token.objects.create(user=instance)


class Tag(models.Model):
    """
    Tag for data. Every tag has unique text
    """
    name = models.SlugField(unique=True)

    def __str__(self):
        return self.name


def calculate_path(self, filename):
    """
    Método que calcula la ruta donde se almacenaran
    los documentos subidos por los usuarios
    """
    return 'users/%s/documents/%s' % (self.owner.id, filename)


class Document(models.Model):
    file = models.FileField(upload_to=calculate_path)
    title = models.CharField(max_length=140)
    description = models.TextField(blank=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='documents')
    tags = models.ManyToManyField(Tag, related_name='documents')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
