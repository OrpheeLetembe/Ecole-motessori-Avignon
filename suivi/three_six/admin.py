from django.contrib import admin


from .models import PracticalLife, SensoryMaterial, Math, Langage, Letter, Comments


class VpAdmin(admin.ModelAdmin):
    list_display = ('id', 'student')


class MsAdmin(admin.ModelAdmin):
    list_display = ('id', 'student')


class MathAdmin(admin.ModelAdmin):
    list_display = ('id', 'student')


class LanAdmin(admin.ModelAdmin):
    list_display = ('id', 'student')


class LtAdmin(admin.ModelAdmin):
    list_display = ('id', 'student')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'student')


admin.site.register(PracticalLife, VpAdmin )
admin.site.register(SensoryMaterial, MsAdmin)
admin.site.register(Math, MathAdmin)
admin.site.register(Langage, LanAdmin)
admin.site.register(Letter, LtAdmin)
admin.site.register(Comments, CommentAdmin)

