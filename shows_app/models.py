from django.db import models

from datetime import datetime, date

class ShowManager(models.Manager):
    def validator(self, postData):
        errors = {}

        if len(postData['title']) < 4:
            errors["title"] = 'Title should be at least 4 characters'
        if self.filter(title__iexact=postData['title']).exists():
            errors["title"] = 'A show with this title already exists.'
        if len(postData['network']) < 4:
            errors["network"] = 'Network should be at least 4 characters'
        if len(postData['description']) > 0 and len(postData['description']) < 10:
            errors["description"] = 'Description should be at least 10 characters'
        
        date_format = '%Y-%m-%d'
        try:
            release_date = datetime.strptime(postData['release_date'], date_format).date()
        except ValueError:
            errors["release_date"] = 'Date must be present'
        else:
            if release_date > date.today():
                errors["release_date"] = 'Release date cannot be in the future.'
        

        return errors

class Show(models.Model):
    title = models.CharField(max_length=48)
    network = models.CharField(max_length=48)
    release_date = models.DateField()
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()


