from django.db import models  # type: ignore

class Department(models.Model):
    """Department describing the user department."""
    title = models.CharField(max_length=100)

class Employee(models.Model):
    """Employee who will be doing competency assessments."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    birthdate = models.DateField(null=True, blank=True)

class KeyArea(models.Model):
    """Key area of focus for the competency."""
    title = models.CharField(max_length=100)

class FunctionalArea(models.Model):
    """Functional area of the competency."""
    title = models.CharField(max_length=100)
    key_area = models.ForeignKey(KeyArea, on_delete=models.CASCADE, default=None)

class Competency(models.Model):
    """Competency for users to attain skill in."""
    title = models.CharField(max_length=100)
    functional_area = models.ForeignKey(FunctionalArea, on_delete=models.CASCADE, default=None)

class Level(models.Model):
    """Level of competency available."""
    title = models.CharField(max_length=100)

class LevelDescription(models.Model):
    """Description of the level in the competency."""
    title = models.CharField(max_length=100)
    competency = models.ForeignKey(Competency, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)

