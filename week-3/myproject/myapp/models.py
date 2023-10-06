from django.db import models

# Create your models here.
class UserComments(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length = 100)
    comment = models.TextField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name