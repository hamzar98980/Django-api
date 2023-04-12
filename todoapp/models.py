from django.db import models

# Create your models here.


class product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    price = models.IntegerField()
    timestamp = models.DateTimeField(
        auto_now_add=True, auto_now=False, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']
