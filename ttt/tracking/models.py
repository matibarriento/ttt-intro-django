from django.db import models


class Track(models.Model):
    """For the NSA"""
    title = models.CharField(max_length=50)
    observation = models.TextField()
    tracked_on = models.DateTimeField()
    audited = models.BooleanField(default=False)
