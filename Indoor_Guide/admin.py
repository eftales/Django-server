from django.contrib import admin
from .models import class_map
from .models import class_probe

# Register your models here.
admin.site.register(class_map)
admin.site.register(class_probe)
