from django.db import models
from django.contrib.auth.models import User


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
    product_name = models.CharField(max_length=200,null=True,blank=True)
    product_price = models.DecimalField(max_digits=6, decimal_places=2,null=True,blank=True)
    phon_number = models.CharField(max_length=10,default='phon_number',null=True,blank=True)
    product_detail = models.TextField(default='No description',null=True,blank=True)
    product_size = models.CharField(max_length=200, default='Default Size',null=True,blank=True)
    product_status = models.ForeignKey(Status, on_delete=models.CASCADE, blank=True,null=True)
    product_statustype = models.CharField(max_length=200,null=True,blank=True)
    product_location = models.CharField(max_length=200, default='location')
    image = models.ImageField(upload_to='Parcel', default='broken_image.png',null=True,blank=True)
   

    def __str__(self) -> str:
        return f'Product {self.product_name}'


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Cart for {self.user.username}'

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(AllProduct, on_delete=models.CASCADE)  # สมมติว่ามีโมเดล Product สำหรับสินค้า
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=6, decimal_places=2,null=True,blank=True)
    
    # price = models.DecimalField(max_digits=10, decimal_places=2)

    # def __str__(self):
    #     return f'{self.quantity} x {self.product.name}'

    # def subtotal(self):
    #     return self.quantity * self.price


