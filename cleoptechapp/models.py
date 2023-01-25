from django.db import models
from django.contrib.auth.models import User


class Product (models.Model):
    product_name=models.CharField( default="", max_length=50)
    category=models.CharField(default="", max_length=50)
    company=models.CharField(default="", max_length=50)
    rate=models.IntegerField(default=1)
    price=models.IntegerField(default=0)
    desc=models.CharField(max_length=500)
    pub_date=models.DateTimeField()
    img=models.ImageField(upload_to='shop/images' ,default='')
    def  __str__ (self):
        return self.product_name

class comment (models.Model):
    body=models.CharField(max_length=100)
    comment_date=models.DateTimeField(auto_now_add=True)
    product= models.ForeignKey(Product, on_delete=models.CASCADE)
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    
    def  __str__ (self):
        return '  %s  %s'%(self.product,self.user_id)


   
    