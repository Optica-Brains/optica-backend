from django.contrib import admin
from .models import Batch, User , Branch ,Order


# Register your models here.
admin.site.register(User)
admin.site.register(Branch)
admin.site.register(Order)
admin.site.register(Batch)

