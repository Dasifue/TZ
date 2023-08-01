from django.db import models

# Модель продукта.
# Я не стал прописывать сложную модель, так как для ТЗ нет необходимости
# Я хотел прописать ещё и категории одеждны, размеры, но решил модель оставить абстрактной

class Product(models.Model):
    image = models.ImageField("Image", upload_to="media/uploads/products/", default="media/default/product.jpg") #Поле image - это картинка продукта. Загружаются фотографии в media, в случае, если создаётся продукт без картинки, то берётся дефолтная картинка  
    name = models.CharField("Name", max_length=255) # Название продукта. Обычный заголовок на 255 элементов
    description = models.TextField("Description", null=True) #Описание - это текст без лимита на количестов элементов
    uploaded = models.DateTimeField("Uploaded", auto_now_add=True) #Дата добавления продукта в магазин
    price = models.DecimalField("Price", decimal_places=2, max_digits=12, null=False) #Цена - decimal, где всего 12 цифр, из которых 2 стоят после точки
    is_available = models.BooleanField("Availability", default=True, null=False) #Статус продукта. Доступность / наличие

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.name
    
    @property
    def short_description(self):
        """
        Проперти метод преображает метод в атрибут.
        Здесь метод выводит первые 40 элементов из описания
        """
        description = self.description.strip() #избавляемся от возможных пробелов слева и справа
        return description[:41]
