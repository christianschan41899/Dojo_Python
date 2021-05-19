from django.db import models
import re

class UserManager(models.Manager):
    def register_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        for data in postData:
            if len(postData[data]) == 0:
                errors['postData'] = "Invalid registration! Please fill out all fields in the form."
        if len(postData['fName']) < 2:
            errors['fName'] = "Invalid registered first name! Must be 2 characters or more!"
        if len(postData['lName']) < 2:
            errors['lName'] = "Invalid registered last name! Must be 2 characters or more!"
        if not EMAIL_REGEX.match(postData['email']): 
            errors['email'] = "Invalid registered email address!"
        if len(postData['pword'])<8:
            errors['pword'] = "Invalid registered password! Must be 8 characters or more!"
        if postData['pword'] != postData['pword_confirm']:
            errors['pword_confirm'] = "Passwords do not match!"
        return errors

class TravelTripManager(models.Manager):
    def trip_validator(self, postData):
        errors = {}
        if len(postData['dest']) < 3:
            errors['dest'] = "Invalid destination! Must contain 3 characters or more!"
        if len(postData['plan']) < 3:   
            errors['plan'] = "Your plan is too short (less than 3 characters)!"
        if len(postData['start']) <= 0:
            errors['start'] = "You can't start a trip without a date to start it at!"
        if len(postData['end']) <= 0:
            errors['end'] = "Unfortunately, our company does not support endless trips!"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    objects = UserManager()

class TravelTrip(models.Model):
    destination = models.CharField(max_length=255)
    plan = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    users = models.ForeignKey(User, related_name = "trips", on_delete = models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now = True)
    objects = TravelTripManager()
