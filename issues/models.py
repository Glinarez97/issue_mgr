from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy

class Status(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=256)
    
    def __str__(self):
        return self.name
    
class Priority(models.Model):
    name = models.CharField(max_length=128)  # Corrected typo: max_length
    description = models.CharField(max_length=256)  # Corrected typo: max_length
    
    def __str__(self):
        return self.name
    
class Issue(models.Model):
    summary = models.CharField(max_length=256)
    description = models.TextField()
    status = models.ForeignKey(
        Status,
        on_delete=models.CASCADE
    )
    priority = models.ForeignKey(  # Changed 'Priority' to lowercase 'priority'
        Priority,
        on_delete=models.CASCADE
    )
    reporter = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    assignee = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="assignee"
    )
    
    def __str__(self):
        return self.summary
    
    def get_absolute_url(self):
        return reverse_lazy("detail", args=[self.id])
