from django.contrib import admin
from django.contrib.admin import StackedInline
from django.utils.translation import gettext_lazy as _
from django.utils.html import format_html
from datetime import datetime
from dateutil import relativedelta
from .models import Ad, User, Category, Address, Conversation, Message, Mission


class AdInline(StackedInline):
    model = Ad
    verbose_name_plural = _('Ads')
    show_change_link = True
    extra = 0

class MissionInline(StackedInline):
    model = Mission
    verbose_name_plural = _('Missions')
    show_change_link = True
    extra = 0


class AddressInline(StackedInline):
    model = Address
    verbose_name_plural = _('Addresses')
    show_change_link = True
    extra = 0

class MessageInline(StackedInline):
    model = Message
    verbose_name_plural = _('Messages')
    show_change_link = True
    extra = 0


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', '_name', '_age', 'phone', '_address_full', 'updated', 'created')
    readonly_fields = ('created', 'updated')
    search_fields = ('email', 'first_name', 'last_name')
    list_display_links = ['email', '_name']
    ordering = ('created',)
    inlines = [
        AdInline,
        AddressInline,
        MissionInline
    ]

    def _name(self, obj):
        output = '{}. {}'.format(
            obj.first_name[0:1],
            obj.last_name
        )
        return output
    _name.short_description = _('Name')

    def _age(self, obj):
        output = '--'
        if obj.birth_date:
            my_birth_date = obj.birth_date
            diff = relativedelta.relativedelta(datetime.now(), my_birth_date)

            output = format_html('<strong>{}</strong> ans'.format(
                diff.years,
            ))
        return output
    _age.short_description = _('Age')

    def _address_full(self, obj):
        output = '{}'.format(
            obj.address
        )
        return output
    _address_full.short_description = _('Address')


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'type', 'status', 'updated', 'created')
    readonly_fields = ('created', 'updated', 'user')
    list_filter = ('user', 'category', 'type', 'status')
    search_fields = ('title', 'description')
    list_display_links = ['user', 'title']
    ordering = ('created',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name', 'description')

@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    list_display = ('ad', 'updated', 'created')
    inlines = [MessageInline]

@admin.register(Mission)
class MissionAdmin(admin.ModelAdmin):
    list_display = ('ad', 'customer', 'updated', 'created')
    search_fields = ('ad', 'customer')

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'content', 'conversation', 'updated', 'created')
    search_fields = ('sender', 'conversation')
