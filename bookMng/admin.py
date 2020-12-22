from django.contrib import admin

# Register your models here.

from .models import MainMenu
from .models import Book
from .models import Review


admin.site.register(MainMenu)
admin.site.register(Review)
admin.site.register(Book)

