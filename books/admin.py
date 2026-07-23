from django.contrib import admin
from .models import Book, Review


# Register your models here.
class ReviewInline(admin.TabularInline):
    model = Review
    extra = 1
     
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "price"]
    search_fields = ["title", "athor"]
    list_filter = ["price"]
    inlines = [ReviewInline]
    

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass
    