from django.db import models

class Condutor(models.Model):
    name  = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(max_length=100, null=False, blank=False)
    address = models.TextField(blank=True, null=True);
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name

