from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Associado(models.Model):
    numero_associado = models.CharField(max_length=10)
    nome = models.CharField(max_length=40)
    telefone = models.CharField(max_length=15, blank=True)
    celular = models.CharField(max_length=15)
    email = models.EmailField(null=False)

    def __str__(self):
        return self.nome
