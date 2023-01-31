from django.db import models

class User(models.Model):
    nome = models.CharField('nome', max_length=50)
    telefone = models.IntegerField('telefone', max_length=15)
    email = models.CharField('email', max_length=40)

    def __str__(self):
        return f'Usuário: {self.nome}, Telefone: {self.telefone}, E-mail{self.email}'
