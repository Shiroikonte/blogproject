from pickle import NONE
from random import choices
from sre_constants import CATEGORY
from django.db import models
from django import forms

CATEGORY = (('business','ビジネス'),('life','生活'),('other','その他'))
class BlogModel(models.Model): #継承
    title = models.CharField(max_length=100)
    content = models.TextField()
    postdate = models.DateField(auto_now_add=True)
    category = models.CharField(
        max_length = 50,
        choices = CATEGORY
    )
    def __str__(self):
        return self.title



