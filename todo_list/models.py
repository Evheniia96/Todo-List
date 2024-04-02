from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.CharField(max_length=255)
    datetime = models.DateTimeField(auto_now_add=True)
    deadline = models.DateField(null=True, blank=True)
    is_done = models.BooleanField()
    tag = models.ManyToManyField(Tag, related_name="tasks")

    class Meta:
        ordering = ["is_done", "-datetime"]

    def __str__(self):
        return f"{self.content[:10]}..."
