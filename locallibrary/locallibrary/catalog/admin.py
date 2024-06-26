from django.contrib import admin

# Register your models here.
from .models import Author, Genre, Book, BookInstance, Language

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    # fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]

    fieldsets = (
        (None, {
            'fields': ('first_name', 'last_name')
        }),
        ('Life Infromation', {
            'fields': ('date_of_birth', 'date_of_death')
        }),
    )

class BookInstanceInline(admin.TabularInline):
    model = BookInstance

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BookInstanceInline]

class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'book_status', 'book_date', 'id')
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )

admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre)
admin.site.register(BookInstance, BookInstanceAdmin)
admin.site.register(Language)