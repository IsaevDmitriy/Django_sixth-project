from django.db import models


class Project(models.Model):
    """Объект на котором проводят измерения."""

    name = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f'{self.name}'

class Measurement(models.Model):
    """Измерение температуры на объекте."""

    value = models.FloatField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f'{self.project} - {self.value}'