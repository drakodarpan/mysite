from django.contrib import admin
from .models import Bookmark, Tag


class BookmarkAdmin(admin.ModelAdmin):
    # Estos campos se mostrarán en vista de lista
    list_display = ('url', 'title', 'owner', 'is_public', 'date_updated',)
    # Estos campos se pueden editar en la vista de lista
    list_editable = ('is_public',)
    # Estos campos pueden ser filtrados en la vista de lista en base a sus valores. Los elementos del filtro se mostrarán en una columna al lado derecho
    list_filter = ('is_public', 'owner__username')
    # Estos campos se pueden buscar en la vista de lista en base a sus valores. Un campo de búsqueda se mostrará por encima de la lista
    search_field = ('title', 'description',)
    # Estos campos no pueden ser editados en la vista de detalle
    readonly_fields = ('date_created', 'date_updated')

    
admin.site.register(Bookmark, BookmarkAdmin)
admin.site.register(Tag)