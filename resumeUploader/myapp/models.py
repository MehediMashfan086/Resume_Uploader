from django.db import models

# Create your models here.

STATE_CHOICES = (
    ('Barisal','Barisal'),
    ('Chittagong','Chittagong'),
    ('Comilla','Comilla'),
    ('Dhaka','Dhaka'),
    ('Gazipur','Gazipur'),
    ('Khulna','Khulna'),
    ('Mymensingh','Mymensingh'),
    ('Narayanganj','Narayanganj'),
    ('Rajshahi','Rajshahi'),
    ('Rangpur','Rangpur'),
    ('Sylhet','Sylhet'),
)

class Resume(models.Model):
    name = models.CharField(max_length = 100)
    dob = models.DateField()
    gender = models.CharField(max_length = 10)
    locality = models.CharField(max_length = 100)
    city = models.CharField(max_length = 100)
    zipcode = models.PositiveIntegerField()
    state = models.CharField(choices = STATE_CHOICES, max_length = 100)
    mobile = models.PositiveIntegerField()
    email = models.EmailField()
    job_city = models.CharField(max_length = 100)
    profile_image = models.ImageField(upload_to = 'profileimg', blank = True)
    my_file = models.FileField(upload_to = 'doc_folder', blank = True)
