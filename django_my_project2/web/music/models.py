from django.db import models

from django.db import models

class Music(models.Model):
    title = models.CharField('Название', max_length=234)
    artist_name = models.TextField('Артитс', blank=True, null=True)
    date = models.DateTimeField('Дата Выхода')    
    image = models.ImageField('Обложка', blank=True, upload_to='images')
    link = models.URLField('Ссылка', blank=True)

    class Meta:
        verbose_name = "Музыка"
        verbose_name_plural = "Музыка"

    def __str__(self):
        return self.title
