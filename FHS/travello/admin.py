from django.contrib import admin
from . models import Destination,Hotels, Item, Option,Room,Section

# Register your models here.

admin.site.register(Destination)
admin.site.register(Hotels)
admin.site.register(Room)
admin.site.register(Section)
admin.site.register(Option)
admin.site.register(Item)