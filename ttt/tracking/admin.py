from django.contrib import admin
from tracking.models import Track
# Register your models here.


class TrackAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'tracked_on', 'audited',)
    list_filter = ('tracked_on', 'audited',)
    search_fields = ('title',)
    date_hierarchy = 'tracked_on'
    ordering = ('-tracked_on',)


admin.site.register(Track, TrackAdmin)
