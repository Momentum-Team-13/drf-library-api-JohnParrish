from django.contrib import admin
from .models import User, Book, Tracking, Note
# Register your models here.

admin.site.register(User)
admin.site.register(Book)
admin.site.register(Tracking)
admin.site.register(Note)
