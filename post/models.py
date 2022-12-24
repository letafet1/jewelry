from django.db import models
from  django.contrib.auth import get_user_model

User=get_user_model()

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name="category_name",null=True)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name="Category"
        verbose_name_plural="Categories"
        ordering=["-id"]

class Prods (models.Model):


    user=models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    name=models.CharField(max_length=200,verbose_name="prods_name",null=True )
    price=models.IntegerField(null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, related_name="post_category", related_query_name="pcategory")
    image = models.ImageField(upload_to="pos_img", null=True)
    description=models.TextField(null=True)
    sale = models.IntegerField(null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name="Prod"
        verbose_name_plural="Prods"
        ordering=["-id"]
