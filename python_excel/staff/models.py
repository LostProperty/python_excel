from django.db import models


TITLE_CHOICES = (
    ('Mr', 'Mr'),
    ('Ms', 'Ms'),
    ('Miss', 'Miss'),
    ('Mrs', 'Mrs')
)

class Job(models.Model):
    title = models.CharField(max_length=20)

    def __unicode__(self):
        return self.title


class Staff(models.Model):
    title = models.CharField(max_length=3, choices=TITLE_CHOICES)
    first_name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    job = models.ForeignKey('Job')

    def __unicode__(self):
        return '{0} {1} {2}'.format(self.title, self.first_name, self.surname)

    class Meta:
        verbose_name_plural = 'staff'
