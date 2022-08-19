from sqlite3 import Date
from django.contrib import admin
from .models import Post, Category, BigCategory,Comment,DateCategory
# Register your models here.

admin.site.register(Post)
admin.site.register(Comment)


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}  # 이렇게 하면 Category 모델의 name필드에 값이 입력됐을 떄 자동으로 slug가 만들어짐

admin.site.register(Category, CategoryAdmin)

class BigCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'bigslug': ('bigname',)}
    
admin.site.register(BigCategory, BigCategoryAdmin)
admin.site.register(DateCategory)