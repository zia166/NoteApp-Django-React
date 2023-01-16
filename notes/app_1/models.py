from django.db import models

# Create your models here.
class Notes(models.Model):
    Body = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = [ "created"]
        
    def __str__(self):
        return self.Body