from django.db import models
from django.utils.text import slugify

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=200, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.category_name)
        super(Category,self).save(*args, **kwargs)
    def __str__(self) :
        return self.category_name
    
class LocationVariant(models.Model):
    variant_name = models.CharField(max_length=20)
    def __str__(self) :
        return self.variant_name


class OpenningVariant(models.Model):
    openning_name = models.CharField(max_length=100)
    def __str__(self) :
        return self.openning_name



class Job(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    job_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='static/jobs')
    salary = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    stock = models.IntegerField(default=50)

    location_type = models.ForeignKey(LocationVariant , blank=True, null=True, on_delete=models.PROTECT)
    openning_type = models.ForeignKey(OpenningVariant , blank=True, null=True, on_delete=models.PROTECT)


    def __str__(self) :
        return self.job_name

   