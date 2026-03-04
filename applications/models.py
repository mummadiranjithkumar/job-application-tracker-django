from django.db import models


class JobApplication(models.Model):
    STATUS_CHOICES = [
        ("Applied", "Applied"),
        ("Interview", "Interview"),
        ("Rejected", "Rejected"),
        ("Offer", "Offer"),
    ]

    company = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    application_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Applied")
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.company} - {self.role}"

