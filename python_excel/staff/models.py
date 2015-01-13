from django.db import models


TITLE_CHOICES = (
    ('Mr', 'Mr'),
    ('Ms', 'Ms'),
    ('Miss', 'Miss'),
    ('Mrs', 'Mrs')
)

class Job(models.Model):
    title = models.CharField(max_length=20, choices=TITLE_CHOICES)


class Staff(models.Model):
    title = models.CharField(max_length=3, choices=TITLE_CHOICES) # null=False
    first_name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    job = models.ForeignKey('Job')
