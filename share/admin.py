from django.contrib import admin
from .models import Item, Catalogue



admin.site.register(Catalogue)
admin.site.register(Item)