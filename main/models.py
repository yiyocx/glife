# coding=utf-8
from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager


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
    owner = models.ForeignKey(User, related_name='documents')
    tags = TaggableManager()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
