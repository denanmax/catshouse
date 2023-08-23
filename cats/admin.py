from django.contrib import admin

from cats.models import Cat, Categories


# Register your models here.
@admin.register(Cat)
class CatAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'dob', 'photo',)
    list_filter = ('name',)


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)
    list_filter = ('name',)
