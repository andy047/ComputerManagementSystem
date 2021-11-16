from django.db import models

# Create your models here.
class Device(models.Model):
    serial = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    hard_disk = models.CharField(max_length=255)
    CPU = models.CharField(max_length=255)
    memory = models.CharField(max_length=255)

    def __str__(self):
        return (f"""{self.serial} {self.brand} {self.model}""")


