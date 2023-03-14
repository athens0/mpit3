from django.db import models


class Movies(models.Model):
    name = models.CharField('Название', max_length=100)
    author = models.CharField('Автор', max_length=100)
    description = models.TextField('Описание')
    publish_date = models.DateField('Дата выхода')
    duration = models.PositiveIntegerField('Длительность')
    rates_count = models.PositiveIntegerField('Количество отзывов')
    rates_sum = models.PositiveIntegerField('Сумма оценок')
    trailer_url = models.CharField('URL Трейлера', max_length=250)
    url = models.CharField('URL Фильма', max_length=250)
    reviews = models.JSONField()
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"


class Reviews(models.Model):
    movie_id = models.PositiveBigIntegerField('Фильм')
    author = models.CharField('Автор', max_length=20)
    rate = models.PositiveIntegerField('Оценка')
    text = models.TextField('Комментарий')
    
    def __str__(self):
        return self.movie_id
    
    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
