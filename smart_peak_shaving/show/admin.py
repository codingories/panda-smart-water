from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(client)
admin.site.register(problem_sort)
admin.site.register(problem_detail)
admin.site.register(item_name)
