from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50,null=True)
    slug = models.SlugField(max_length=50,null=True,unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class News(models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name='Xeber basligi', help_text='Basligi daxil edin')
    category = models.ForeignKey(Category,null=True,on_delete=models.DO_NOTHING)
    description = models.TextField(blank=False,null=False,verbose_name='Xeberi daxil edin')
    image = models.ImageField(upload_to="news/%Y/%m/%d/",)
    date = models.DateTimeField(auto_now_add=True)
    available = models.BooleanField(default=True)

    
    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'
