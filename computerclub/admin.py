from django.contrib import admin
from .models import Director, Administrator, User, Order

admin.site.register(Director)
admin.site.register(Administrator)
admin.site.register(User)
admin.site.register(Order)

