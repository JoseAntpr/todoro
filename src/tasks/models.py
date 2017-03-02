from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Task(models.Model):

    PENDING = "PEN"
    DONE = "DON"
    STATUSES = (
        (PENDING, "Pending"),
        (DONE,"Done")
    )
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=3, default=PENDING, choices=STATUSES)
    time_estimated = models.IntegerField(null=True)
    deadline = models.DateField(null=True)
    created_at = models.DateTimeField(auto_now_add=True) # Automaticamente se añade la fecha de creación.
    modified_at = models.DateTimeField(auto_now=True) # Automáticamente se actualiza la fecha al guardar.
    owner = models.ForeignKey(User, related_name="owned_tasks")
    assignee = models.ForeignKey(User, null=True, default= None, related_name="assigned_tasks")

    def __str__(self):
        return self.name