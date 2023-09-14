# from django.db import models
# from django.urls import reverse

# class Categories(models.Model):
#     name = models.CharField(max_length=100)
#     image = models.FileField(blank=True, null=True, upload_to='stock-flow-category-image')
#     # number = models.IntegerField(unique=True, db_index=True)

#     def __str__(self):
#         return self.name

#     def get_absolute_url(self):
#         return reverse('category')
# class Product(models.Model):
#     name = models.CharField(max_length=100)
#     purchaseCost = models.DecimalField(decimal_places=3, max_digits=10)
#     salePrice = models.DecimalField(decimal_places=3, max_digits=10)
#     image = models.FileField(blank=True, null=True, upload_to='stock-flow-product-image')
#     categoryId = models.ForeignKey(Categories , on_delete=models.PROTECT)

#     def __str__(self):
#         return self.name

#     def get_absolute_url(self):
#         return reverse('productList')