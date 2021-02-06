from django.contrib import admin
from .models import *


# admin.site.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name', 'date_of_birth']


class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'display_genre']
    list_filter = ['genre', 'author']


class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ['show_id', 'book', 'status']
    list_filter = ['status', 'due_back']


admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(BookInstance, BookInstanceAdmin)
admin.site.register(Genre)

# Register your models here.
