from django.db import models



STATUSTYPE = (
        ('พร้อมเช่า', 'พร้อมเช่า'),
        ('ไม่พร้อมเช่า', 'ไม่พร้อมเช่า'),
    )

class Course(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self) -> str:
        return f'{self.name}'
    
class Status(models.Model):
    name_Status = models.CharField(max_length=100, default="", blank=True)

    def __str__(self):
        return f'{self.name_Status}'
           

class AllProduct(models.Model):
    id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=200)
    product_price = models.DecimalField(max_digits=6, decimal_places=2)
    phon_number = models.CharField(max_length=10,default='phon_number')
    product_detail = models.TextField(default='No description')
    product_size = models.CharField(max_length=200, default='Default Size')
    # product_status = models.ForeignKey(Status, on_delete=models.CASCADE, default=" ", blank=True)
    product_statustype = models.CharField(max_length=200, choices = STATUSTYPE, default=" ")
    product_location = models.CharField(max_length=200, default='location')
    image = models.ImageField(upload_to='Parcel', blank=True, null=True, default='broken_image.png')

    def __str__(self) -> str:
        return f'Product {self.product_name}'


