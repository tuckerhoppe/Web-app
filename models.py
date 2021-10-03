from django.db import models

# Create your models here.
class dicecompanionItem(models.Model):
    content = models.TextField()
    content1 = 'monkey'

class Customer(models.Model):
    enter_number = models.CharField(max_length=200)
    

    def __str__(self):
        return self.first_name + ' ' +self.last_name