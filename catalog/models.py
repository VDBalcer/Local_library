from django.db import models
from django.urls import reverse
import uuid


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


class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), help_text="Unique ID for this particular book across whole library")
    book = models.ForeignKey('Book', on_delete=models.SET_NULL(), null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(blank=True)
    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available')
        ('r', 'Reserved')
    )
    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m', help_text='Book availability')
    class Meta:
        ordering = ["due_back"]

    def __str__(self):
        return f'{self.id} : {self.book.name}'