from django.contrib import admin

from .models import Post

# регистрируем посты на панели администрирования
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass
