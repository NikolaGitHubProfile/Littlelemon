from django.db import models

# Create your models here.
class Booking(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=255)
    no_of_guests = models.SmallIntegerField()
    bookingdate = models.DateTimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.name
 
class Menu(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()
    
    def __str__(self):
        return self.title