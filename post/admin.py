from django.contrib import admin
from .models import Prods, Category

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):

    class Meta:
        model = Category

    list_display = ("title",)


admin.site.register(Category, CategoryAdmin)

class ProdsAdmin(admin.ModelAdmin):

    class Meta:
        model = Prods

    list_display = ("name","category", "description")


admin.site.register(Prods, ProdsAdmin)
