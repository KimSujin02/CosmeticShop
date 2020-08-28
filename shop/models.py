from django.db import models
from django.shortcuts import resolve_url


class Category(models.Model) :
    # 속성 아이메이크업 베이스메이크업 립메이크업
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, allow_unicode=True, unique=True) #url에 내 카테고리 이름이 보이게.. 아이디처럼 움직임 겹치면 안됨. => UNIQUE

    # class Meta
    class Meta :
        ordering = ['name']
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    # __str__
    def __str__(self):
        return self.name

    # get_absolute_url()
    def get_absolute_url(self):
        return resolve_url('shop:product_in_category', self.slug)
    

class Product(models.Model):
    # name
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, allow_unicode=True, unique=True)
    # price
    price = models.DecimalField(max_digits=10, decimal_places=2) #100원 $9.99
    # category
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='products')
    # image
    image = models.ImageField(upload_to='products/%y/%m/%d', default='products/no_image.jpg')
    # stock
    stock = models.PositiveIntegerField()
    # description 설명
    description = models.TextField(blank=True)

    available_display = models.BooleanField('Display', default=True)
    available_order = models.BooleanField('Order', default=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return resolve_url('shop:product_detail', self.id, self.slug)