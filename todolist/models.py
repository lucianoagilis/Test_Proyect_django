from django.db import models


class Item(models.Model):
    description = models.CharField(max_length=200)
    done = models.BooleanField(default=False)

