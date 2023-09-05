from django.db import models

# Create your models here.
NULLABLE = {'blank': True, 'null': True}


class Categories(models.Model):
    name = models.CharField(max_length=120, verbose_name='Имя')
    description = models.TextField(**NULLABLE, verbose_name='Описание')
    photo = models.ImageField(upload_to='categories/', verbose_name='Фото', **NULLABLE, )

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Порода'
        verbose_name_plural = 'Породы'


class Cat(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, verbose_name='Порода')
    photo = models.ImageField(upload_to='cats/', verbose_name='Фото', **NULLABLE, )
    dob = models.DateField(**NULLABLE, verbose_name='ДР')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Кошка'
        verbose_name_plural = 'Кошки'


class Parent(models.Model):
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, verbose_name='Имя')
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, verbose_name='Порода')
    birth_day = models.DateField(**NULLABLE, verbose_name='Дата рождения')

    def __str__(self):
        return f'{self.name} ({self.category})'

    class Meta:
        verbose_name = 'предок'
        verbose_name_plural = 'предки'
