from django.contrib import admin
from blogapp.models import BlogPost
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    exclude = ('slug',)
    list_display = ['id','title','date_created']
    ordering = ['date_created']
admin.site.register(BlogPost, BlogAdmin)