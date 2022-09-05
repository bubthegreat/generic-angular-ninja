from django.db import models  # type: ignore

class StringConfig(models.Model):
    """Level of competency available."""

    title = models.CharField(max_length=100)
    value = models.CharField(max_length=255)


class IntConfig(models.Model):
    """Description of the level in the competency."""

    title = models.CharField(max_length=100)
    value = models.IntegerField(default=-1)


class UserProfile(models.Model):
    """User profile information"""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    about_me = models.CharField(max_length=2048)
