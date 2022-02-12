from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Dealer(models.Model):
    rel = models.ForeignKey(User, on_delete=models.CASCADE);
    
    name = models.CharField(max_length=100)
    mob = models.CharField(max_length=20)
    nature = models.CharField(max_length=50)
    weight = models.IntegerField()
    
    from_state = models.CharField(max_length=100)
    from_city = models.CharField(max_length=100)
    to_state = models.CharField(max_length=100)
    to_city = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Driver(models.Model):
    rel = models.ForeignKey(User, on_delete=models.CASCADE);
    
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    mob = models.CharField(max_length=20)
    truck_no = models.CharField(max_length=20)
    truck_capacity = models.IntegerField()
    transporter_name =models.CharField(max_length=100)
    driving_experience = models.IntegerField()
    
    from_state1 = models.CharField(max_length=100)
    from_city1 = models.CharField(max_length=100)
    to_state1 = models.CharField(max_length=100)
    to_city1 = models.CharField(max_length=100)
    
    from_state2 = models.CharField(max_length=100)
    from_city2 = models.CharField(max_length=100)
    to_state2 = models.CharField(max_length=100)
    to_city2 = models.CharField(max_length=100)
    
    from_state3 = models.CharField(max_length=100)
    from_city3 = models.CharField(max_length=100)
    to_state3 = models.CharField(max_length=100)
    to_city3 = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Book(models.Model):
    dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)