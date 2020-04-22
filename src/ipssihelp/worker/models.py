from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser


# Create your models here.

# User
class User(AbstractUser):
    username = models.CharField(
        verbose_name=_('Username'),
        max_length=100,
        unique=False,
        blank=True,
        null=True,
    )
    email = models.EmailField(
        verbose_name=_('Email'),
        max_length=100,
        unique=True,
    )
    gender = models.CharField(
        max_length=1,
        choices=(
            ('w', _('Women')),
            ('m', _('Man')),
            ('o', _('Other')),
        ),
        blank=True,
        null=True,
        verbose_name=_('Gender')
    )
    phone = models.CharField(
        max_length=16,
        blank=True,
        null=True,
        verbose_name=_('Phone')
    )
    birth_date = models.DateField(
        blank=True,
        null=True,
        verbose_name=_('Birth date')
    )
    updated = models.DateTimeField(
        auto_now=True,
        editable=False,
        verbose_name=_('Updated date')
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')
        db_table = 'user'
        unique_together = ['email', 'phone']
        indexes = [
            models.Index(fields=[
                'email',
                'phone',
            ]),
        ]

    def __str__(self):
        return '{}. {}'.format(
            self.first_name[0],
            self.last_name
        )


# Address
class Address(models.Model):
    address1 = models.CharField(
        max_length=255,
        blank=False,
        verbose_name=_('Address 1')
    )
    address2 = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name=_('Address 2')
    )
    postal_code = models.CharField(
        max_length=255,
        blank=False,
        verbose_name=_('Postal Code')
    )
    city = models.CharField(
        max_length=255,
        verbose_name=_('City')
    )
    country = models.CharField(
        max_length=128,
        blank=False,
        null=False,
        default='FR',
        verbose_name=_('Country'),
        help_text='ISO Alpha-2'
    )
    latitude = models.DecimalField(
        max_digits=8,
        decimal_places=3,
        blank=True,
        null=True,
        verbose_name=_('Latitude')
    )
    longitude = models.DecimalField(
        max_digits=8,
        decimal_places=3,
        blank=True,
        null=True,
        verbose_name=_('Longitude')
    )
    updated = models.DateTimeField(
        auto_now=True,
        editable=False,
        verbose_name=_('Update date')
    )
    created = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        verbose_name=_('Created date')
    )
    user = models.OneToOneField(
        'User',
        null=True,
        on_delete=models.PROTECT,
        verbose_name=_('User')
    )

    class Meta:
        verbose_name = _('Address')
        verbose_name_plural = _('Addresses')
        indexes = [
            models.Index(fields=['address1', 'postal_code']),
        ]
        db_table = 'address'

    def __str__(self):
        return '{}. {} - {}'.format(
            self.address1,
            self.city,
            self.country
        )


# Category
class Category(models.Model):
    name = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        verbose_name=_('Title')
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name=_('Description')
    )

    class Meta:
        ordering = ['name']
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')
        db_table = 'category'
        indexes = [
            models.Index(fields=[
                'name',
            ]),
        ]

    def __str__(self):
        return str(self.name)


# Ad
class Ad(models.Model):
    title = models.CharField(
        max_length=128,
        blank=False,
        null=False,
        verbose_name=_('Title')
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name=_('Description')
    )
    category = models.ForeignKey(
        'Category',
        on_delete=models.PROTECT,
        blank=True,
        verbose_name=_('Category')
    )
    type = models.CharField(
        max_length=32,
        choices=(
            ('supply', _('Supply')),
            ('demand', _('Demand')),
        ),
        default='supply',
        verbose_name=_('Type')
    )
    status = models.CharField(
        blank=True,
        null=True,
        max_length=32,
        choices=(
            ('waiting', _('Waiting')),
            ('online', _('Online')),
            ('canceled', _('Canceled')),
        ),
        default='waiting',
        verbose_name=_('Status')
    )
    updated = models.DateTimeField(
        auto_now=True,
        editable=False,
        verbose_name=_('Updated date')
    )
    created = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        verbose_name=_('Created date')
    )
    user = models.ForeignKey(
        'User',
        on_delete=models.PROTECT,
        blank=False,
        null=False,
        verbose_name=_('User')
    )

    class Meta:
        verbose_name = _('Ad')
        verbose_name_plural = _('Ads')
        db_table = 'ad'
        indexes = [
            models.Index(fields=[
                'title',
                'status',
            ]),
        ]

    def __str__(self):
        return '{} - {}'.format(
            self.title,
            self.pk
        )

    @property
    def is_supply(self):
        if self.type == 'supply':
            return True

    @property
    def is_demand(self):
        if self.type == 'demand':
            return True


# Conversation
class Conversation(models.Model):
    updated = models.DateTimeField(
        auto_now=True,
        editable=False,
        verbose_name=_('Updated date')
    )
    created = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        verbose_name=_('Created date')
    )
    ad = models.ForeignKey(
        'Ad',
        on_delete=models.PROTECT,
        blank=False,
        null=False,
        verbose_name=_('Ad')
    )

    class Meta:
        verbose_name = _('Conversation')
        verbose_name_plural = _('Conversations')
        db_table = 'conversation'

    def __str__(self):
        return '{} - {}'.format(
            self.pk,
            self.ad
        )


# Message
class Message(models.Model):
    content = models.TextField(
        blank=True,
        null=True,
        verbose_name=_('Content')
    )
    updated = models.DateTimeField(
        auto_now=True,
        editable=False,
        verbose_name=_('Updated date')
    )
    created = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        verbose_name=_('Created date')
    )
    conversation = models.ForeignKey(
        'Conversation',
        on_delete=models.PROTECT,
        blank=False,
        null=False,
        verbose_name=_('Conversation')
    )
    sender = models.ForeignKey(
        'User',
        on_delete=models.PROTECT,
        blank=False,
        null=False,
        verbose_name=_('User')
    )

    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = _('Messages')
        db_table = 'message'

    def __str__(self):
        return 'Message - {}'.format(
            self.conversation
        )


# Mission
class Mission(models.Model):
    updated = models.DateTimeField(
        auto_now=True,
        editable=False,
        verbose_name=_('Update date')
    )
    created = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        verbose_name=_('Created date')
    )
    ad = models.ForeignKey(
        'Ad',
        on_delete=models.PROTECT,
        blank=False,
        null=False,
        verbose_name=_('Ad')
    )
    customer = models.ForeignKey(
        'User',
        on_delete=models.PROTECT,
        blank=False,
        null=False,
        verbose_name=_('User')
    )

    class Meta:
        verbose_name = _('Mission')
        verbose_name_plural = _('Missions')
        db_table = 'mission'

    def __str__(self):
        return '{} - {}'.format(
            self.ad,
            self.customer
        )
