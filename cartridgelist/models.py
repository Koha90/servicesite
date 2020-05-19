from django.db import models
from django.contrib.auth.models import User
import uuid

# Cartridges
class Cartridges(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4())
    date_of_repairs = models.DateField()
    address = models.CharField(max_length=250)
    total = models.IntegerField()
    client = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        ordering = ['-date_of_repairs']

    def __str__(self):
        return self.address
