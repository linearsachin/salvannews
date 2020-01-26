from django.contrib import admin
from .models import  NewsData, Category,IP
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title','category')
    list_filter = (
        
        'category','time','website',
    )



admin.site.register(NewsData,CategoryAdmin)
admin.site.register(Category)
admin.site.register(IP)
