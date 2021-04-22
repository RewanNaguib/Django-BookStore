from django.contrib import admin
from .models import Booklet,Category,Isbn,Note
from .forms import BookletForm,CategoryForm


class BookletAdmin (admin.ModelAdmin):
    form=BookletForm
    list_display=("title","author","content")
    list_filter=("categories",)
    search_fields=("title",)

class BookletInLine(admin.StackedInline):
    model=Booklet
    max_num=3
    extra=1

class NoteAdmin(admin.ModelAdmin):
    inlines=[BookletInLine]

class CategoryAdmin(admin.ModelAdmin):
    form=CategoryForm    

admin.site.register(Booklet,BookletAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Isbn)
admin.site.register(Note,NoteAdmin)



