from django.db import models  # type: ignore

class StringConfig(models.Model):
    """Level of competency available."""

    title = models.CharField(max_length=100)
    value = models.CharField(max_length=255)


class IntConfig(models.Model):
    """Description of the level in the competency."""

    title = models.CharField(max_length=100)
    value = models.IntegerField(default=-1)

