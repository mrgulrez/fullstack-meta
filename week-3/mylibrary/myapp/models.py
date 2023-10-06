from django.db import models
from datetime import datetime

# Create your models here.
class Book(models.Model):
    title = models.CharField(db_column='title', max_length=100, blank=False)
    description = models.TextField(db_column='description', max_length=10000, blank=False)
    author = models.CharField(db_column='author', max_length=100, blank=False)
    year = models.IntegerField(db_column='year', blank=False)
    published_date = models.DateTimeField(db_column='published_date', default=datetime.now, blank=False)
