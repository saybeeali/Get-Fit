from django.contrib import admin
from .models import Bodypart, Exercise , Routine

# Register your models here.
admin.site.register(Bodypart)
admin.site.register(Exercise)
admin.site.register(Routine)