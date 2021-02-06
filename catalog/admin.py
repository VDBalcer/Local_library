from django.contrib import admin
from .models import *


class BookInline(admin.TabularInline):
    model = Book
    extra = False

class AuthorAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name', 'date_of_birth']
    fields = ['last_name', 'first_name', ('date_of_birth', 'date_of_death')]
    inlines = [BookInline]


class BookInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = False


class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'display_genre']
    list_filter = ['genre', 'author']
    inlines = [BookInstanceInline]


class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ['show_id', 'book', 'status']
    list_filter = ['status', 'due_back']
    exclude = ['id']
    fieldsets = (
        (None, {
            'fields': ['book', 'imprint']
        }),
        ('Доступность книги', {
            'fields': ['status', 'due_back']
        })
    )


admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(BookInstance, BookInstanceAdmin)
admin.site.register(Genre)

# Register your models here.
