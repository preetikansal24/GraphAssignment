from django.db import models


class Trackers(models.Model):
    created_at = models.DateField(blank=True, null=True, auto_now=True, auto_now_add=False)
    updated_at = models.DateField(blank=True, null=True, auto_now=False, auto_now_add=True)

    class Meta:
        abstract = True
