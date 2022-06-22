from django.contrib import admin


from .models import Ambiance

class AbianceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'year')


admin.site.register(Ambiance, AbianceAdmin)