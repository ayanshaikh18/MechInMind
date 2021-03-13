from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin

from . import models

admin.site.register(models.Category)
admin.site.register(models.SubCategory)
admin.site.register(models.Article, MarkdownxModelAdmin)
