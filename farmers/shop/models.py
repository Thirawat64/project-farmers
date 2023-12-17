from django.db import models

class Course(models.Model):
    
    name = models.CharField(max_length=300)
    

    def __str__(self) -> str:
        return f' {self.name} '
    
class AllProduct(models.Model):
    product_name = models.CharField(max_length=200)
    product_price = models.IntegerField(primary_key=True,max_length=200)
    product_detail = models.TextField(null=True,blank=True)
    #img_product = models.ImageField(upload_to='product_images/')

    def __str__(self) -> str:
        return f' {self.product_name} '