from django.db import models
from django.utils.html import mark_safe
from django.contrib.auth.models import User
# Create your models here.

class Banner(models.Model):
    img = models.ImageField(upload_to="banners/")
    alt_text = models.CharField(max_length = 200)

#here we are returning the name of the image in admin panel 
    def __str__(self):
        return self.alt_text
#here we are returning the image of the image in admin panel 
    def image_tag(self):
        return mark_safe('<img src ="%s" "width = "50" />' % (self.img.url))

class Service(models.Model):
    title = models.CharField(max_length =150)
    img = models.ImageField(upload_to="services/", null=True)
    details = models.TextField()

    #here we are returning the name of the image in admin panel 
    def __str__(self):
        return self.title
#here we are returning the image of the image in admin panel 
    def image_tag(self):
        return mark_safe('<img src ="%s" "width = "50" />' % (self.img.url))


class Pages(models.Model):
    title = models.CharField(max_length =150)
    details = models.TextField()

    #here we are returning the name of the image in admin panel 
    def __str__(self):
        return self.title
    

class FAQ(models.Model):
    ques = models.TextField()
    ans = models.TextField()

    #here we are returning the name of the image in admin panel 
    def __str__(self):
        return self.ques
    
class Enquiry(models.Model):
    full_name = models.CharField(max_length = 100)
    email = models.CharField(max_length = 50)
    details = models.TextField()
    send_time = models.DateTimeField(auto_now_add=True)

    #here we are returning the name of the image in admin panel 
    def __str__(self):
        return self.full_name    


class Gallery(models.Model):
    title = models.CharField(max_length =150)
    img = models.ImageField(upload_to="Gallery/", null=True)
    details = models.TextField()

    #here we are returning the name of the image in admin panel 
    def __str__(self):
        return self.title
#here we are returning the image of the image in admin panel 
    def image_tag(self):
        return mark_safe('<img src ="%s" "width = "50" />' % (self.img.url))


class GalleryImages(models.Model):
    gallery = models.ForeignKey(Gallery, on_delete = models.CASCADE, null = True)
    alt_text = models.CharField(max_length =150)
    img = models.ImageField(upload_to="Gallery_mgs/", null=True)

    #here we are returning the name of the image in admin panel 
    def __str__(self):
        return self.alt_text
#here we are returning the image of the image in admin panel 
    def image_tag(self):
        return mark_safe('<img src ="%s" "width = "50" />' % (self.img.url))

class SubPlan(models.Model):
    title = models.CharField(max_length =150)
    max_member = models.IntegerField(null = True)
    price = models.IntegerField()

    def __str__(self):
        return self.title

class SubPlanFeature(models.Model):
    subplan = models.ForeignKey(SubPlan, on_delete=models.CASCADE)
    title = models.CharField(max_length =150)

    
    def __str__(self):
        return self.title


class PlanDiscount(models.Model):
    subplan = models.ForeignKey(SubPlan, on_delete=models.CASCADE, null =True)
    total_month = models.IntegerField()
    total_discount = models.IntegerField()

    def __str__(self):
        return str(self.total_month)
    


class Subscriber(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE, null =True)
        mobile = models.CharField(max_length=20, null = True)
        address = models.TextField(null = True)
        img = models.ImageField(upload_to="profile/", null = True)

        def __str__(self):
           return str(self.user)
    

        def image_tag(self):
          return mark_safe('<img src ="%s" "width = "50" />' % (self.img.url))


class Subscription(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE, null =True)
        plan = models.ForeignKey(SubPlan, on_delete=models.CASCADE, null =True)
        price = models.CharField(max_length= 50, null = True)


