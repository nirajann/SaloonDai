from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    digital = models.BooleanField(default=False,null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    @property
    def imageURl(self):
        try:
            url = self.image.url
        except:
            url = ''
            return url
    
    def __str__(self):
    	return self.name


  
class contactform(models.Model):
    id=models.AutoField(auto_created=True,primary_key=True)
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=200)
    subject = models.CharField(max_length=100)
    messgae = models.CharField(max_length=500)


