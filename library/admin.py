from django.contrib import admin

from library.models import Book, CustomUser

admin.site.register(Book)
admin.site.register(CustomUser)