from django.db import models

# Create your models here.

# Create your models here.

class Catalogue(models.Model):
    catalogue_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.catalogue_text


class Item(models.Model):
    catalogue = models.ForeignKey(Catalogue, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=200,unique=True)
    item_url = models.CharField(max_length=200)
    item_conf = models.CharField(max_length=200,default='Unknown')
    item_reader = models.CharField(max_length=200)
    item_date = models.IntegerField(default=0)
    item_description = models.TextField(max_length=2000)
    pub_date = models.DateField('data published')
    def __str__(self):
        return self.item_name