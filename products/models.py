from django.db import models
from random import randint


class Cakmak(models.Model):
    MATERYAL_TERCIHLERI = [
        ('Plastik', 'Plastik'),
        ('Metal', 'Metal')
    ]

    FONKSIYON_TERCIHLERI = [
        ('Taşlı', 'Taşlı'),
        ('Manyetolu', 'Manyetolu'),
        ('Rezistanslı', 'Rezistanslı')
    ]

    marka = models.CharField(blank=True, max_length=200)
    model = models.CharField(blank=True, max_length=200)
    no = models.IntegerField(
        primary_key=True, unique=True, editable=False)
    materyal = models.CharField(max_length=200, choices=MATERYAL_TERCIHLERI)
    fonksiyon = models.CharField(max_length=200, choices=FONKSIYON_TERCIHLERI)
    fiyat = models.DecimalField(max_digits=15, decimal_places=2)
    adet = models.IntegerField()
    ana_foto = models.ImageField(upload_to='fotolar/%Y/%m/%d/')
    foto_2 = models.ImageField(upload_to='fotolar/%Y/%m/%d/', blank=True)
    foto_3 = models.ImageField(upload_to='fotolar/%Y/%m/%d/', blank=True)
    foto_4 = models.ImageField(upload_to='fotolar/%Y/%m/%d/', blank=True)
    foto_5 = models.ImageField(upload_to='fotolar/%Y/%m/%d/', blank=True)
    foto_6 = models.ImageField(upload_to='fotolar/%Y/%m/%d/', blank=True)
    aciklama = models.CharField(max_length=1000, blank=True)
    online = models.BooleanField(default=True)
    insert = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.no is None:
            while True:
                number = randint(100000, 999999)
                if Cakmak.objects.filter(no=number).exists():
                    print('Number exists')
                else:
                    self.no = number
                    break
            super(Cakmak, self).save(*args, **kwargs)
        else:
            super(Cakmak, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-no']
        verbose_name = 'Çakmak'
        verbose_name_plural = 'Çakmaklar'

    def __str__(self):
        return (self.marka) + (' ') + (self.model)


class Marka(models.Model):
    marka = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Marka'
        verbose_name_plural = 'Markalar'

    def __str__(self):
        return (self.marka)
