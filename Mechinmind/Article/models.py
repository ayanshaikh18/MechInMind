from datetime import datetime

from django.db import models
from markdownx.models import MarkdownxField


# Create your models here.


class Category(models.Model):
    Id = models.AutoField(primary_key=True)
    Name = models.CharField(null=False, max_length=100)

    def __str__(self):
        return self.Name


class SubCategory(models.Model):
    Id = models.AutoField(primary_key=True)
    Name = models.CharField(null=False, max_length=100)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    CoverPhoto = models.ImageField(upload_to="images/", default="images/blog-2.png", verbose_name="Cover Picture")
    Description = models.TextField(default="Description...")

    def __str__(self):
        return self.Name


class Article(models.Model):
    Id = models.AutoField(primary_key=True)
    Title = models.CharField(null=False, max_length=100)
    Views = models.IntegerField(default=0)
    ShortDescription = models.TextField(max_length=50, default="short desc")
    HighlightText = models.TextField(max_length=50, null=True)
    Description = MarkdownxField()
    SubCategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    CoverPhoto = models.ImageField(upload_to="images/", default="images/5.jpg", verbose_name="Cover Picture")
    UploadDate = models.DateField(default=datetime.now().date())

    def __str__(self):
        return self.Title
