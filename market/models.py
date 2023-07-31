from django.db import models
from django.utils import timezone
from django.conf import settings

class Version(models.Model):
    game_version = models.CharField(max_length = 200)

    def __str__(self):
        return self.game_version
    
class Type(models.Model):
    service_type = models.CharField(max_length = 200) 

    def __str__(self):
        return self.service_type

class Product(models.Model):
    service_name = models.CharField(max_length = 200)
    game_version = models.ForeignKey('Version', on_delete = models.SET_NULL, null=True)
    service_type = models.ForeignKey('Type', on_delete = models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discription = models.TextField()
    is_favorite = models.BooleanField(default=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(upload_to ='products/%Y/%m/%d', blank = True)
    created_date = models.DateTimeField(auto_now_add = True)
    updated_date = models.DateTimeField(auto_now = True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.service_name
       
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)
    average_rating = models.DecimalField(max_digits=3, decimal_places=2, default=0)

class Rating(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='ratings')
    rating = models.IntegerField()

class Review(models.Model):
       author = models.CharField(max_length=100)
       content = models.TextField()
       product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')

class Favorite(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.product.service_name}"
    
    class Meta:
        unique_together = ('user', 'product')
