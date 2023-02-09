from django.db import models
from django.contrib.auth.models import AbstractUser
from accounts.utils import UserManager

class County(models.Model):
    county_name = models.CharField(max_length=80)
    county_code = models.PositiveBigIntegerField()
    logo = models.ImageField(upload_to='accounts/counties/logos/')

    def __str__(self) -> str:
        return self.county
    
    def logo_url(self) -> str:
        return self.logo.url

class Location(models.Model):
    county = models.ForeignKey(County, on_delete=models.CASCADE)
    constituency = models.CharField(max_length=80)
    constituency_code = models.PositiveBigIntegerField()

    def __str__(self) -> str:
        return self.constituency

class UserProfile(AbstractUser):
    username = None
    email = models.EmailField(('email address'), unique=True)
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    bio = models.TextField()
    phone_number = models.CharField(max_length=10, default='07XXXXXXX')
<<<<<<< HEAD
    national_id = models.PositiveBigIntegerField(default='00000000')
    # location = models.ForeignKey(Location, on_delete=models.CASCADE, )
    avatar = models.FileField(upload_to='accounts/user/avatar/', null=True)
=======
    # national_id = models.PositiveBigIntegerField()
    # location = models.ForeignKey(Location, on_delete=models.CASCADE)
    avatar = models.FileField(upload_to='accounts/user/avatar/')
>>>>>>> fdda34ce18b39e2fae6395d699673b6e9a2d916c
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self) -> str:
        return self.email
    
    def get_avatar_url(self) -> str: # image url
        return self.avatar.url
    

    class Meta:
        db_table = 'user_profiles'
