from django.db import models


class Banner(models.Model):
    image = models.ImageField(upload_to='banner/')
    discount=models.PositiveSmallIntegerField(default=1)
    title = models.CharField(max_length=64)
    info =models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        db_table = 'banners'
        verbose_name = 'banner'
        verbose_name_plural = 'banners'

    def __str__(self):
        return f"{self.id}|{self.title}"