from django.db import models

# Create your models here.
class DebugModel(models.Model):
    string = models.CharField(max_length=24)

    class Meta:
        verbose_name_plural = 'debuggers'

    def __str__(self):
        return self.string