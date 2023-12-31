from django.db import models

# Create your models here.


class Training(models.Model):
    title = models.CharField(max_length=200)
    duration = models.IntegerField()  # minutes
    distance = models.DecimalField(decimal_places=2, max_digits=5)  # km

    def __str__(self):
        return self.title
