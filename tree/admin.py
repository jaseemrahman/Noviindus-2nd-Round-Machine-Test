from django.contrib import admin
from tree.models import Book
from mptt.admin import MPTTModelAdmin
from mptt.admin import DraggableMPTTAdmin

# Register your models here.
# admin.site.register(Book)
admin.site.register(
    Book,
    DraggableMPTTAdmin,
    list_display=(
        'tree_actions',
        'indented_title',
        # ...more fields if you feel like it...
    ),
    list_display_links=(
        'indented_title',
    ),
)
