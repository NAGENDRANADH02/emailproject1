# Create your models here.
from django.db import models

class EmailTemplate(models.Model):
    title = models.CharField(max_length=255)  # Title of the email
    content = models.TextField()             # Main content of the email
    footer = models.TextField(blank=True, null=True)  # Footer section of the email (optional)
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for when the template was created
    updated_at = models.DateTimeField(auto_now=True)      # Timestamp for when the template was last updated

    def __str__(self):
        return self.title
