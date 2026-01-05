from .models import Book

# Register your models here.
admin.site.register(Book)


# Customize the admin interface
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pablished_year')
    search_fields = ('title', 'author')
    list_filter = ('published_year',)
    
admin.site.register(Book, BookAdmin)
