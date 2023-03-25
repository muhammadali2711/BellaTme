import random
import string

from django.db import models

# Create your models here.
from django.utils.text import slugify

from base.db import Default
from base.helper import default_lang


class Category(Default):
    content = models.JSONField(max_length=128, default=default_lang())
    slug = models.SlugField(max_length=128, unique=True, blank=True)
    is_main = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.content.get("en"))
            while True:
                try:
                    root = Category.objects.get(slug=self.slug)
                except:
                    root = None

                if not root:
                    break
                else:
                    strr = str(self.content.get("en")) + "_" + ''.join(random.choice(string.digits) for i in range(10))
                    self.slug = slugify(strr)
        return super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.slug}"

    class Meta:
        verbose_name = "Category"


class Teacher(Default):
    name = models.CharField(max_length=128)
    desc = models.JSONField(default=default_lang())
    img = models.ImageField(upload_to='teachers')

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Teacher"


class AboutCourse(models.Model):
    name = models.JSONField(default=default_lang())
    desc = models.JSONField(default=default_lang())
    img = models.ImageField(upload_to='about_course')

    class Meta:
        verbose_name = "Course"

    def __str__(self):
        return f"{self.name['en']}"


class AboutVacancy(models.Model):
    name = models.JSONField(default=default_lang())
    desc = models.JSONField(default=default_lang())
    img = models.ImageField(upload_to='about_course')

    def __str__(self):
        return f"{self.name['en']}"

    class Meta:
        verbose_name = "Course"


class OnlineWork(models.Model):
    img = models.ImageField(upload_to='online_work')
    desc = models.JSONField(default=default_lang())

    def __str__(self):
        return f"{self.desc['en']}"


class Why(models.Model):
    title = models.JSONField(default=default_lang())
    desc = models.JSONField(default=default_lang())
    img = models.ImageField(upload_to='why')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title['en']


class Partner(models.Model):
    company = models.CharField(max_length=256)
    logo = models.ImageField(upload_to='sayt')
    social = models.JSONField(default={"telegram": "", "instagram": "", "web": "", "facebook": ""})

    def __str__(self):
        return self.company


class Sifat(models.Model):
    title = models.JSONField(default=default_lang())
    desc = models.JSONField(default=default_lang())
    type = models.IntegerField(choices=(
        (1, "For kids"),
        (2, "For teens"),
    ), default=1)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title['en']


class Rating(models.Model):
    img = models.ImageField(upload_to='parents')
    name = models.CharField(max_length=128)
    rating = models.IntegerField(choices=(
        (1, "⭐"),
        (2, "⭐⭐"),
        (3, "⭐⭐⭐"),
        (4, "⭐⭐⭐⭐"),
        (5, "⭐⭐⭐⭐⭐"),
    ), default=1)
    opinion = models.TextField()

    def __str__(self):
        return self.name
