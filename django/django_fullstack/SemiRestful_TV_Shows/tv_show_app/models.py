from django.db import models

class tvShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        for data in postData:
            if len(postData[data]) == 0:
                errors['postData'] = "Invalid submit! Please fill out all fields in the form."
        if len(postData['title']) < 2:
            errors['title'] = "Invalid title! Must be 2 characters or more!"
        if len(postData['network']) < 3:
            errors['network'] = "Invalid network name! Must be 3 characters or more!"
        if len(postData['desc']) < 10:
            errors['desc'] = "Invalid description! Must be 10 characters or more!"
        
        return errors

class tvShow(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateField()
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = tvShowManager()
# Create your models here.


