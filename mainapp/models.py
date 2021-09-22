from django.db import models
import datetime

def century_range():
    return [(parseCentury(c),parseCentury(c)) for c in range(-40, centuryFromYear(datetime.date.today().year+100)) if c != 0]

def centuryFromYear(year):
    if year>=0:
        return (year) // 100 + 1
    else:
        return (year-1) // 100

def parseCentury(i):
    j = str(abs(i))
    if i > 0:
        return j + 'C'
    else:
        return j + 'BC'

class Country(models.Model):
    country = models.CharField(max_length=50)
    def __str__(self):
        return f'{self.country}'
    class Meta:
        verbose_name_plural = "countries"

class Location(models.Model):
    city = models.CharField(max_length=50)
    country =  models.ForeignKey(Country, on_delete=models.CASCADE) # CASCADE or SET_NULL
    def __str__(self):
        return f'{self.city},{self.country}'

class Visitor(models.Model):
    email = models.EmailField()
    date = models.DateField()
    def __str__(self):
        return f'{self.email} ({self.date})'

# Create your models here. (one table per model)
class Item(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    organizer_email = models.EmailField()
    description = models.TextField()
    image = models.ImageField(upload_to='images') #pointer of a local image file
    century = models.CharField(max_length=10, choices=century_range(), default=parseCentury(centuryFromYear(datetime.date.today().year)))
    location = models.ForeignKey(Location, on_delete=models.CASCADE) # one-to-many / CASCADE or SET_NULL
    visitors = models.ManyToManyField(Visitor, blank=True, null=True)
    image_url = models.CharField(max_length=500)

    def __str__(self):
        return f'{self.title} - {self.slug}'