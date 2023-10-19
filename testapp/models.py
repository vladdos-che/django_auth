from django.db import models


class Message(models.Model):
    text = models.CharField(verbose_name='Сообщение', max_length=100)

    def __str__(self):
        return self.text

