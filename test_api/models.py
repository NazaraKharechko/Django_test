from django.db import models


class OrdersModel(models.Model):
    class Meta:
        db_table = 'orders_model'

    date_order_creation = models.DateField()
    goods = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.goods}'


class UsersModel(models.Model):
    class Meta:
        db_table = 'users_model'

    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=30)
    date_birth = models.DateField()
    date_registration = models.DateField()
    order = models.ForeignKey(OrdersModel, on_delete=models.CASCADE)

    # Можливість завантаження користувачів з файлу
    # file = models.FileField(null=True, verbose_name='file ', blank=True)

    def __str__(self):
        return f'{self.name}'


class Person(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    birth_date = models.DateField()
    date_registration = models.DateField()
    order = models.ForeignKey(OrdersModel, on_delete=models.CASCADE)
