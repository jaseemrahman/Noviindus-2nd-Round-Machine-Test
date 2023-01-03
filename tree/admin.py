from django.contrib import admin
from tree.models import Book
from mptt.admin import MPTTModelAdmin

# Register your models here.
admin.site.register(Book,MPTTModelAdmin)

