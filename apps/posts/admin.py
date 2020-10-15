from django.contrib import admin

from .models import Like,Rating,Comment
# Register your models here.

admin.site.register(Like)
admin.site.register(Rating)
admin.site.register(Comment)