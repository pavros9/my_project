from django.conf import settings
from django.db import models
from django.utils import timezone
from django.core.files.storage import FileSystemStorage
from django import forms

class TimeStampMixin(models.Model):
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    anons = models.CharField('Анонс', max_length=150)
    full_text = models.TextField('Текст')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField('Дата', auto_now=True)
   

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural ='Посты'



class Article(models.Model):
     img = models.ImageField('Фото', upload_to='images/', blank=True)
     content = models.TextField('Текст')

     class Meta:
        verbose_name = 'Обо мне'
        verbose_name_plural ='Обо мне'

class Quiz(models.Model):
    gender = models.CharField('Пол', max_length=10)
    age = models.CharField('Возраст', max_length=15)
    rating = models.IntegerField('Рейтинг')

    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural ='Опросы'


    