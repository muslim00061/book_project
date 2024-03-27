from django.db import models

class Book(models.Model):
    name = models.CharField("Кітаптың аты", max_length=50)
    discription = models.TextField("Описание")
    image = models.CharField("Ссылка на изображения", max_length=1000)
    price = models.IntegerField("Цена")

    def __str__(self):
        return self.name

