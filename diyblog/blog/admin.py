from django.contrib import admin
from blog.models import Blogger, Blog

# Register your models here.
# admin.site.register(Blogger)
# admin.site.register(Blog)

@admin.register(Blogger) # decorator to register the models...does exact same this as 'admin.site.register(Blogger, BloggerAdmin)  
class BloggerAdmin(admin.ModelAdmin):
    list_display = ('username',)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'post_date')
    list_filter = ('post_date', 'author')