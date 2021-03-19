from django.db import models

class Outlet(models.Model):
    id = models.AutoField(primary_key=True)
    outletname = models.CharField(max_length=30)
    foodtype = models.CharField(max_length=20)
    homedelivery = models.CharField(max_length=5, default='No')
    ownerfirstname = models.CharField(max_length=20)
    ownerlastname = models.CharField(max_length=20)
    address = models.TextField()
    addresslink = models.URLField()
    iframeaddress = models.TextField(default="")
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    verified = models.BooleanField(default=True)
    image = models.ImageField(upload_to=(''))
    def __str__(self):
        return self.outletname
