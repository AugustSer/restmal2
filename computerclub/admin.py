from django.contrib import admin
from .models import Director, Administrator, User_test, Order

admin.site.register(Director)
admin.site.register(Administrator)
admin.site.register(User_test)
admin.site.register(Order)

