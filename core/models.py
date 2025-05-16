from django.db import models
from django.utils import timezone

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100, blank=True)
    company_name = models.CharField(max_length=100, blank=True)  # ✅ New Field
    quote = models.TextField()
    approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.company_name or self.role or 'Testimonial'}"