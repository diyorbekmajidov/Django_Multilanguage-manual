from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Concert)
admin.site.register(ConcertCategory)
admin.site.register(Ticket)