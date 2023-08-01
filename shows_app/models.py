from django.db import models

class ShowManager(models.Manager):
    def validator(self, postData):
        errors = {}

        if len(postData['title']) < 4:
            errors["title"] = 'Title should be at least 4 characters'
        if len(postData['network']) < 10:
            errors["network"] = 'Network should be at least 10 characters'
        
        return errors

class Show(models.Model):
    title = models.CharField(max_length=48)
    network = models.CharField(max_length=48)
    release_date = models.DateField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()


