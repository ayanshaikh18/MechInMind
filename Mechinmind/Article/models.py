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

    def __str__(self):
        return self.Name


class Article(models.Model):
    Id = models.AutoField(primary_key=True)
    Title = models.CharField(null=False, max_length=100)
    Views = models.IntegerField(default=0)
    Description = MarkdownxField()
    SubCategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.Title
