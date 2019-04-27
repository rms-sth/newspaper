from django.contrib import admin
from .models import Category, Topic, Post, Tag
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.

admin.site.register(Category)
admin.site.register(Topic)
admin.site.register(Tag)

# Apply summernote to all TextField in model.


class SomeModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'


admin.site.register(Post, SomeModelAdmin)
