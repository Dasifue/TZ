from django.db import models

class Product(models.Model):
    image = models.ImageField("Image", upload_to="media/uploads/products/", default="media/default/product.jpg")
    name = models.CharField("Name", max_length=255)
    description = models.TextField("Description", null=True)
    uploaded = models.DateTimeField("Uploaded", auto_now_add=True)
    price = models.DecimalField("Price", decimal_places=2, max_digits=12, null=False)
    is_available = models.BooleanField("Availability", default=True, null=False)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.name
