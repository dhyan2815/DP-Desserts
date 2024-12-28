from django.contrib import admin
from app.models import Order, MenuItem

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'date')
    filter_horizontal = ('items',)  # Makes the 'items' field more user-friendly in the admin panel

admin.site.register(MenuItem)
admin.site.register(Order, OrderAdmin)