import os
from django.db import models
from django.contrib.gis.db import models as gismodels

# Create your models here.

class Departments(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256)
    status = models.IntegerField(help_text="0=active;1=inactive;2=delete")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'app_departments'

def product_image_upload_path(instance, filename):
    return os.path.join(f"api/product/{instance.id}", filename)

class Products(models.Model):
    id = models.AutoField(primary_key=True)
    product_code = models.CharField(max_length=256, default=False)
    brand = models.CharField(max_length=256)
    department = models.ForeignKey(Departments, on_delete=models.CASCADE, related_name='product_department_id')
    generic_names = models.JSONField(max_length=256)
    genericname_general = models.CharField(max_length=256, default=False)
    measure = models.CharField(max_length=256)
    multi_measure = models.BooleanField()
    product_name = models.CharField(max_length=256)
    product_image = models.TextField(max_length=1024, null=True, blank=True)
    upload_image = models.ImageField(upload_to=product_image_upload_path, null=True, blank=True)
    quantity_per_piece = models.IntegerField(default=False, null=True)  # to store null values also
    pieces_per_kg = models.IntegerField(default=False, null=True)
    unit_per_piece = models.CharField(max_length=256, default=False)
    measure_per_piece = models.CharField(max_length=256, default=False)
    quantity = models.FloatField()
    site = models.CharField(max_length=256)
    sku = models.CharField(max_length=256)
    unit = models.CharField(max_length=50)
    status = models.IntegerField(help_text="0=active;1=inactive;2=delete")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'app_products'

class StoreGroups(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256)
    logo = models.CharField(max_length=256)
    status = models.IntegerField(help_text="0=active;1=inactive;2=delete")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'app_storegroups'

class Stores(gismodels.Model):
    id = models.AutoField(primary_key=True)
    store_address = models.CharField(max_length=1000)
    latitude = models.CharField(max_length=256)
    longitude = models.CharField(max_length=256)
    store_group = models.ForeignKey(StoreGroups, on_delete=models.CASCADE, related_name='stores_group_id')
    store_logo = models.CharField(max_length=256)
    store_name = models.CharField(max_length=256)
    store_code = models.CharField(max_length=256, default=False)
    store_zipcode = models.CharField(max_length=256)
    store_location = gismodels.PointField(srid=4326, null=True, blank=True)
    status = models.IntegerField(help_text="0=active;1=inactive;2=delete")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'app_stores'

class StoreProducts(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Products, max_length=259, on_delete=models.CASCADE,
                                related_name='store_product_id')
    store = models.ForeignKey(Stores, max_length=259, on_delete=models.CASCADE, related_name='product_id')
    is_exist = models.BooleanField(default=False)
    new_measure_info = models.JSONField(max_length=256, null=True, blank=True)
    price = models.FloatField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.IntegerField(help_text="0=active;1=inactive;2=delete")