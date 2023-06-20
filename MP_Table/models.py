from django.db import models

# Create your models here.

class People(models.Model):
    date_missing = models.DateField()
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    age_at_missing = models.IntegerField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    gender = models.CharField(max_length=1)
    race = models.CharField(max_length=1)
    
    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)
    
    def __str__(self):
        return '%s | %s | %s | %s | %s | %s | %s | %s' % ( self.date_missing ,self.first_name, self.last_name, self.age_at_missing, self.city, self.state, self.gender, self.race)
    
