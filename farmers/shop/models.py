from django.db import models

class Course(models.Model):
    
    name = models.CharField(max_length=300)
    

    def __str__(self) -> str:
        return f' {self.name} '
    
class AllProduct(models.Model):
    
    product_name = models.CharField(max_length=200)
    product_price = models.IntegerField(primary_key=True, max_length=10)
    product_detail = models.TextField(default='No description')
    product_size = models.CharField(max_length=200,default='Default Size')
    product_status = models.CharField(max_length=200,default='Default status')
    product_location = models.CharField(max_length= 200,default ='location')
    img = models.ImageField(upload_to='product_images',null=True,blank=True)
    
    def __str__(self) -> str:
        return f' {self.product_name} '





    