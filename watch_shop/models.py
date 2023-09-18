from django.db import models

class Shop(models.Model):
    MODEL = (
        ('B650WB-1B', 'B650WB-1B'),
        ('MTP-VD03B-1A', 'MTP-VD03B-1A'),
        ('MTP-1308D-1A', 'MTP-1308D-1A'),
        ('MTP-VD01G-1B', 'MTP-VD01G-1B')
    )
    title = models.CharField('Укажите название часов:', max_length=100)
    description = models.TextField('Описание часов:', blank=True, null=True)
    image = models.ImageField('Добавьте фото часов:', upload_to='images/')
    review = models.URLField('Укажите ссылку')
    model = models.CharField('Укажите модель часов:', max_length=100, choices=MODEL)
    cost = models.PositiveIntegerField('Укажите цену часов:')
    director = models.CharField('Укажите авторство:', max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Часы'
        verbose_name_plural = 'Часы'

