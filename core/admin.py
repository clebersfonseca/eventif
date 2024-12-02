from django.contrib import admin
from django.utils.html import format_html
from core.models import Speaker


class SpeakerModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'photo_img', 'website_link']

    def website_link(self, obj):
        return format_html('<a href="{0}">{0}</a>', obj.website)

    website_link.short_description = 'website'

    def photo_img(self, obj):
        return format_html('<img src="{}" width="32px"/>', obj.photo)

    photo_img.short_description = 'Foto'


admin.site.register(Speaker, SpeakerModelAdmin)
