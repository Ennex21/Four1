from django.db import models
from django.urls import reverse


class Artic2(models.Model):
    title = models.CharField('Название', max_length=50)
    photo = models.ImageField('Фотография', upload_to='imagege/')
    desk = models.TextField('Описание')
    price = models.IntegerField('Цена')

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})


    class Meta:
        verbose_name = 'Игра'
        verbose_name_plural = 'Игры'
        ordering = ['id']



