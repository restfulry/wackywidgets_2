from django.db import models


class Widget(models.Model):
    description = models.CharField(max_length=150)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.description
