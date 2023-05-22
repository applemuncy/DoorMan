from django.contrib import admin

# Register your models here.

from .models import UserProfile, AccessEvent

admin.site.register(UserProfile)

#admin.site.register(AccessEvent)

class AccessEventAdmin(admin.ModelAdmin):
    list_displey = ('user',  'event_date')

admin.site.register(AccessEvent, AccessEventAdmin)

