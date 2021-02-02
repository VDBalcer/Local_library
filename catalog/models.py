from django.db import models
from django.urls import reverse


class Genre(models.Model):
    name = models.CharField(max_length=100, help_text="Введите жанр книги")

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100, help_text="Название книги")
    author = models.ForeignKey('Author', on_delete=models.SET_NULL(), null=True)
    summary = models.TextField(help_text="Введите краткое описание книги")
    isbn = models.CharField('ISBN', max_length=13, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    genre = models.ManyToManyField('Genre', help_text="Выберите жанр книги")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])
