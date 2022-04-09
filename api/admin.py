from django.contrib import admin
<<<<<<< HEAD
from .models import *
=======
from .models import Batch, User , Branch ,Order
>>>>>>> 314b07b6911b3f17715e7a7e3596300c25e46d4e


# Register your models here.
admin.site.register(User)
admin.site.register(Branch)
admin.site.register(Order)
admin.site.register(Batch)

