from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class Settings(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    descriptions = models.CharField(max_length=255, verbose_name="Описание", blank=True, null=True)
    logo = models.ImageField(upload_to='logo/',verbose_name="Логотип", blank=True, null=True)
    image = models.ImageField(upload_to='geeks_image/', verbose_name='Фотография', blank=True, null=True)
    video = models.URLField( verbose_name='видео')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Основная Настройка",
        verbose_name_plural = "Основные Настройки"

class About(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    title1 = models.CharField(max_length=50, verbose_name="Заголовок 1")
    descriptions1 = models.CharField(max_length=255, verbose_name="Описание 1")
    title2 = models.CharField(max_length=50, verbose_name="Заголовок 2")
    descriptions2 = models.CharField(max_length=255, verbose_name="Описание 2")
    image = models.ImageField(upload_to='image/', verbose_name='Фотография')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "О нас",
        verbose_name_plural = "О нас"

class Values(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    title1 = models.CharField(max_length=50, verbose_name="Заголовок 1")
    descriptions1 = models.CharField(max_length=500, verbose_name="Описание 1")
    title2 = models.CharField(max_length=50, verbose_name="Заголовок 2")
    descriptions2 = models.CharField(max_length=500, verbose_name="Описание 2")
    title3 = models.CharField(max_length=50, verbose_name="Заголовок 3")
    descriptions3 = models.CharField(max_length=500, verbose_name="Описание 3")

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Ценность",
        verbose_name_plural = "Ценности"

class Junior(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    title1 = models.CharField(max_length=50, verbose_name="Заголовок 1")
    descriptions1 = models.CharField(max_length=500, verbose_name="Описание 1")
    title2 = models.CharField(max_length=50, verbose_name="Заголовок 2")
    descriptions2 = models.CharField(max_length=500, verbose_name="Описание 2")
    title3 = models.CharField(max_length=50, verbose_name="Заголовок 3")
    descriptions3 = models.CharField(max_length=500, verbose_name="Описание 3")
    title4 = models.CharField(max_length=50, verbose_name="Заголовок 4")
    descriptions4 = models.CharField(max_length=500, verbose_name="Описание 4")

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Junior",
        verbose_name_plural = "Junior"

class Portfolio(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    # descriptions = models.CharField(max_length=255, verbose_name="Описание", blank=True, null=True)
    image = models.ImageField(upload_to='image/',verbose_name="Фото", blank=True, null=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Портфолио",
        verbose_name_plural = "Портфолио"


class Contact(models.Model):
    phone = models.CharField(max_length=30, verbose_name="Телефонный номер")
    instagram = models.URLField(verbose_name="инстаграмм")
    whatsapp = models.URLField(verbose_name="ватсап")
        
    def __str__(self):
        return self.phone

    class Meta:
        verbose_name = "Контакт",
        verbose_name_plural = "Контакты"

class Blog(models.Model):
    title  = models.CharField(
        max_length=255,
        verbose_name="Название"
    )
    image = models.ImageField(
        upload_to="blog_image/",
        verbose_name="Фотография"
    )
    descriptions = RichTextField(
        verbose_name="Информационный текст",
        blank=True,null=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Время",
        blank=True,null=True
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новость",
        verbose_name_plural = "Новости"