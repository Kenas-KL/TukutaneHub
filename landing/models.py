
from django.db import models
from django.utils.text import slugify

# Create your models here.

class SectionActivity(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    def __str__(self): return self.name


class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    section = models.ForeignKey(SectionActivity, on_delete=models.CASCADE)

    def __str__(self): return self.name


class Enterprise(models.Model):
    name = models.CharField(max_length=100)
    image_logo = models.ImageField(upload_to='images/', null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    sections = models.ManyToManyField(SectionActivity)
    services = models.ManyToManyField(Service)
    address = models.CharField(max_length=500)
    latitude = models.CharField(max_length=10, null=True, blank=True)
    longitude = models.CharField(max_length=10, null=True, blank=True)
    slug = models.SlugField(max_length=500, null=True, blank=True)\

    class Meta:
        ordering = ['-pk']


    def save(self, *args, **kwargs):
        if not self.slug or slugify(self.name) != self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Request(models.Model):
    name = models.CharField(max_length=100)
    name_enterprise = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        ordering = ['-created_at']

class Country(models.Model):
    name = models.CharField(max_length=100)
    name_enterprise = models.CharField(max_length=100)
