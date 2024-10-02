from django.db import models
from django.utils.translation import gettext_lazy as _

class ConcertCategory(models.Model):
    name = models.CharField(max_length=64, verbose_name=_('name'))
    description = models.TextField(max_length=256, blank=True, null=True, verbose_name=_("description"))

    VERBOSE_NAME = _('ConcertCategory')
    class Meta:
        verbose_name = _("concert category")
        verbose_name_plural = _("concert categories")
        ordering = ["-name"]

    def __str__(self):
        return f"{self.name}"
    
class Concert(models.Model):
    name = models.CharField(max_length=64, verbose_name=_('name'))
    description = models.TextField(max_length=256, blank=True, null=True, verbose_name=_("description"))
    categories = models.ManyToManyField(ConcertCategory, verbose_name=_("categories"))
    starts_at = models.DateTimeField(verbose_name=_("starts_at"))
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name= _("price"))
    tickets_left = models.IntegerField(default=0, verbose_name=_("tickets_left"))

    VERBOSE_NAME = 'Concert'

    class Meta:
        verbose_name = _("Concert")
        verbose_name_plural = _("Concerts")
        ordering = ["starts_at"]

    def is_sold_out(self):
        return self.tickets_left == 0

    def __str__(self):
        return f"{self.name}"
    
class Ticket(models.Model):
    concert = models.ForeignKey(to=Concert, on_delete=models.CASCADE, verbose_name=_('consert'))
    customer_full_name = models.CharField(max_length=64, verbose_name=_('customer_full_name'))
    PAYMENT_METHODS = [
        ("CC", "Credit card"),
        ("DC", "Debit card"),
        ("ET", "Ethereum"),
        ("BC", "Bitcoin"),
    ]
    payment_method = models.CharField(
        max_length=2, default="CC", choices=PAYMENT_METHODS, verbose_name=_('payment_method')
    )
    paid_at = models.DateTimeField(auto_now_add=True, verbose_name=_("paid_at"))
    is_active = models.BooleanField(default=True, verbose_name=_('is_active'))

    VERBOSE_NAME = 'Ticket'

    class Meta:
        verbose_name = _("Ticket")
        verbose_name_plural = _("Tickets")

    def __str__(self):
        return f"{self.customer_full_name} ({self.concert})"