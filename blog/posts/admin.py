from django.contrib import admin
from .models import Post, Author

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "summary", "published_date", "image")

class AuthorAdmin(admin.ModelAdmin):
    filter_horizontal = ("posts",)


admin.site.register(Post, PostAdmin)
admin.site.register(Author, AuthorAdmin)