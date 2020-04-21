from django.contrib import admin
from django.contrib.admin import StackedInline
from django.utils.translation import gettext_lazy as _
from .models import Ad, User, Category


class AdInline(StackedInline):
    model = Ad
    verbose_name_plural = _('Ads')
    show_change_link = True
    extra = 0


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'phone', 'updated', 'created')
    readonly_fields = ('created', 'updated')
    search_fields = ('email', 'first_name', 'last_name')
    list_display_links = ['email', 'first_name', 'last_name']
    ordering = ('created',)
    inlines = [
        AdInline
    ]


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'type', 'status', 'updated', 'created')
    readonly_fields = ('created', 'updated', 'user')
    list_filter = ('user', 'category', 'type', 'status')
    search_fields = ('title', 'description')
    list_display_links = ['user', 'title']
    ordering = ('created',)


admin.site.register(Category)
