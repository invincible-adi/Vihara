from django.db import models

# Create your models here.

class register(models.Model):
    email=models.CharField(max_length=200,primary_key=True)
    passwd=models.CharField(max_length=100,null=True)

class joins(models.Model):
    Name=models.CharField(max_length=200,null=True)
    Mobile=models.IntegerField(null=True)
    Email=models.CharField(max_length=200,null=True)

class slider(models.Model):
    spic=models.ImageField(upload_to='static/slider/',null=True)
    sdate=models.DateField()

class contact(models.Model):
    Name=models.CharField(max_length=200,null=True)
    Mobile=models.IntegerField(null=True)
    Email=models.CharField(max_length=200,null=True)
    Message=models.TextField(null=True)

class event(models.Model):
    event_picture=models.ImageField(upload_to='static/event/',null=True)
    price=models.IntegerField(null=True)
    dprice=models.IntegerField(null=True)
    event_date=models.CharField(max_length=100,null=True)
    event_time=models.CharField(max_length=100,null=True)
    event_detail=models.TextField(null=True)
    event_des=models.CharField(max_length=500,null=True)
    event_s=models.CharField(max_length=100,null=True)
    event_e=models.CharField(max_length=100,null=True)
    event_category=models.CharField(max_length=100,null=True)
    event_org=models.CharField(max_length=100,null=True)
    event_mob=models.CharField(max_length=200,null=True)
    event_mail=models.CharField(max_length=100,null=True)
    event_add=models.CharField(max_length=500,null=True)
    event_phn=models.CharField(max_length=500,null=True)

class category(models.Model):
    cname=models.CharField(max_length=200,null=True)
    cpic=models.ImageField(upload_to='static/category/',null=True)
    cdate=models.DateField()
    def __str__(self):
        return self.cname

class booknow(models.Model):
    userid=models.CharField(max_length=200,null=True)
    event_name=models.CharField(max_length=400,null=True)
    event_picture=models.CharField(max_length=400,null=True)
    # speaker_name=models.CharField(max_length=200,null=True)
    # city=models.CharField(max_length=50,null=True)
    # hotel=models.CharField(max_length=200,null=True)
    # speaker_picture=models.CharField(max_length=400,null=True)
    event_date=models.CharField(max_length=100,null=True)
    event_price=models.CharField(max_length=500,null=True)
    booking_date=models.DateField()

class register(models.Model):
    email=models.CharField(max_length=200,primary_key=True)
    uname=models.CharField(max_length=200,null=True)
    passwd=models.CharField(max_length=100,null=True)
    upic=models.ImageField(upload_to='static/profile',null=True)
    address=models.TextField(null=True)

class videogallery(models.Model):
    category=models.ForeignKey(category,on_delete=models.CASCADE)
    vlink=models.TextField(null=True)
    vdate=models.DateField()
    event_des=models.TextField(null=True)


