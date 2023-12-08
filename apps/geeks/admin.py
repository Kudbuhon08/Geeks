from django.contrib import admin
from apps.geeks.models import Settings, Contact, About, Values, Junior, Portfolio,Blog

@admin.register(Settings)
class GeeksAdmin(admin.ModelAdmin):
    list_display = ['title', 'descriptions']

@admin.register(About)
class GeeksAdmin(admin.ModelAdmin):
    list_display = ['title', 'title1', 'descriptions1', 'title2', 'descriptions2']

@admin.register(Values)
class GeeksAdmin(admin.ModelAdmin):
    list_display = ['title', 'title1', 'descriptions1', 'title2', 'descriptions2', 'title3', 'descriptions3']

@admin.register(Junior)
class GeeksAdmin(admin.ModelAdmin):
    list_display = ['title', 'title1', 'descriptions1', 'title2', 'descriptions2', 'title3', 'descriptions3', 'title4', 'descriptions4']

@admin.register(Portfolio)
class GeeksAdmin(admin.ModelAdmin):
    list_display = ['title', 'image']

@admin.register(Contact)
class GeeksAdmin(admin.ModelAdmin):
    list_display = ['phone', 'instagram', 'whatsapp']

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'descriptions']
# admin.site.register(Contact)

