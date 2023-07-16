from django.db import models



class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name.upper()

class Items(models.Model):
    name=models.CharField( max_length=70)
    img_path=models.CharField(("Img Path"), max_length=50)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    left_in_stock=models.IntegerField()
    desc=models.TextField()

    def __str__(self):
        return self.name.upper()
    



    
class Orders(models.Model):
    order_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    items=models.CharField(max_length=5000)
    address=models.TextField(max_length=250)
    oid=models.CharField(max_length=50)

    def __str__(self):
        return self.name.upper()
    




