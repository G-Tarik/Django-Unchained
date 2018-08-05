from django.db import models


class Category(models.Model):
    name_text = models.CharField(max_length=100, unique=True)
    description_text = models.CharField(max_length=200)

    def __str__(self):
        return self.name_text


class Item(models.Model):
    PRODUCT = 'product'
    SERVICE = 'service'
    TYPE_CHOICES = (
        (PRODUCT, 'Product'),
        (SERVICE, 'Service'),
        ('', 'Select type'),
    )
    name_text = models.CharField(max_length=100, unique=True)
    description_text = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='items')
    type_text = models.CharField(max_length=7, choices=TYPE_CHOICES)
    opinions_number = models.IntegerField(default=0)

    def __str__(self):
        return self.name_text


class Opinion(models.Model):
    title_text = models.CharField(max_length=100)
    message_text = models.TextField(max_length=500)
    publish_date = models.DateTimeField(auto_now_add=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='opinions')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='opinions')

    def __str__(self):
        return self.title_text

    class Meta:
        ordering = ('-publish_date',)
