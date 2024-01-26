from django.contrib import admin
from .models import HelloKitty, Owner

# Register your models here.
admin.site.register(Owner)
admin.site.register(HelloKitty)