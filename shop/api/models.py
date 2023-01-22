from django.db import models
from simple_history.models import HistoricalRecords
from django.contrib.auth.models import User

import math


class Product(models.Model):
    title = models.CharField(verbose_name='Название товара', max_length=50)
    description = models.TextField(verbose_name='Описание товара')
    category = models.ManyToManyField("Category", verbose_name="Категории")
    price = models.PositiveIntegerField(verbose_name='Цена', default=0)
    image = models.ImageField(
        verbose_name="Логотип компании", upload_to='img/products', default='')
    seller = models.ForeignKey(
        "Seller", verbose_name="Компания", on_delete=models.CASCADE)

    history = HistoricalRecords()

    def get_total_rating(self):
        marks = self.user_stars.count()
        ratings = Rating.objects.filter(product=self)
        total = 0
        arr = []
        for rating in ratings:
            total += rating.stars
        try:
            for i in range(math.floor(total/marks)):
                arr.append(i)
            return arr
        except ZeroDivisionError:
            return arr

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товар'


class Category(models.Model):
    title = models.CharField(verbose_name='Описание категории', max_length=50)
    description = models.TextField(verbose_name='Описание категории')
    image = models.ImageField(
        verbose_name='Фото категории', upload_to='img/categories', default='')

    history = HistoricalRecords()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'


class Seller(models.Model):
    name = models.CharField(
        verbose_name='Наименование товара', max_length=50)
    description = models.TextField(verbose_name='Описание товара')
    contacts = models.TextField(verbose_name='Контакты')

    history = HistoricalRecords()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товар'


class Rating(models.Model):
    creator = models.ForeignKey(
        User, verbose_name='Пользователь', on_delete=models.CASCADE, default=0)
    product = models.ForeignKey(
        Product, verbose_name='Товар', related_name='user_stars', on_delete=models.CASCADE, default=0)
    title = models.CharField(
        verbose_name='Ваше имя', max_length=50)
    text = models.TextField(verbose_name='Ваш вопрос')
    stars = models.PositiveSmallIntegerField(
        verbose_name='Оценка качества обслуживания', default=0)

    history = HistoricalRecords()

    def __str__(self):
        return f'{self.title} - {self.stars}'

    class Meta:
        unique_together = ('creator', 'product')
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Callback(models.Model):
    phone = models.CharField(verbose_name="Номер телефона", max_length=50)
    name = models.CharField(verbose_name="Имя", max_length=50)
    done = models.BooleanField(verbose_name='Звонок выполнен', default=False)

    history = HistoricalRecords()

    def __str__(self):
        return f'{self.name} - {self.done}'

    class Meta:
        verbose_name = 'Звонок'
        verbose_name_plural = 'Звонки'


STATUS_CHOICES = [
    ('Не рассмотрено', 'Не рассмотрено'),
    ('Рассмотрено', 'Рассмотрено'),
]


class Order(models.Model):
    user = models.ForeignKey(
        User, verbose_name='Пользователь', on_delete=models.CASCADE, default=0)
    products = models.ManyToManyField(Product, verbose_name='Товар')
    status = models.CharField(
        verbose_name='Рассмотрено?', choices=STATUS_CHOICES, default='Не рассмотрено', max_length=50)
    total = models.PositiveIntegerField(
        verbose_name='Цена', default=0)

    history = HistoricalRecords()

    def __str__(self):
        return f'{self.id}'

    class Meta:
        verbose_name = 'Отправленная заявка'
        verbose_name_plural = 'Отправленная заявка'


class Basket(models.Model):
    user = models.OneToOneField(
        User, verbose_name='Пользователь', on_delete=models.CASCADE)
    products = models.ManyToManyField(
        Product, verbose_name='Товар', blank=True, default=[])
    subtotal = models.PositiveIntegerField(
        verbose_name='Цена', default=0)

    history = HistoricalRecords()

    def __str__(self):
        return f'Избранное {self.user.username}'

    class Meta:
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранное'
