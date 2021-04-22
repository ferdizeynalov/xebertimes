from django.db import models

# Create your models here.

class Partners(models.Model):
    name = models.CharField(max_length=200, unique=True, help_text='Basligi daxil edin') 
    description = models.TextField(blank=False,null=False)
    image = models.ImageField(upload_to="partners/%Y/%m/%d/",)
    site = models.URLField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.site

    class Meta:
        verbose_name = 'Partner'
        verbose_name_plural = 'Partners'
        ordering = ('-created',)



class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=50)
    subject = models.TextField(max_length=60)
    message = models.TextField()

    def __str__(self):
        return self.email
