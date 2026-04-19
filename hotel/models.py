from django.db import models

class Room(models.Model):
    number = models.IntegerField()
    price = models.FloatField()
    is_busy = models.BooleanField(default=False)

    def str(self):
        return str(self.number)


# 2
class Customer(models.Model):
    name = models.CharField(max_length=100)

    def str(self):
        return self.name


# 3
class Booking(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    days = models.IntegerField()

    def total_price(self):
        return self.days * self.room.price


# 4
class Food(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()

    def str(self):
        return self.name


# 5
class Order(models.Model):
    foods = models.ManyToManyField(Food)

    def total_price(self):
        return sum(food.price for food in self.foods.all())


# 6
class Staff(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=50)

    def str(self):
        return self.name


# 7
class Service(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()

    def str(self):
        return self.name


# 8
class Payment(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    amount = models.FloatField()
    method = models.CharField(max_length=50)

    def str(self):
        return str(self.amount)


# 9
class Review(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    text = models.TextField()

    def str(self):
        return self.text[:20]


# 10
class RoomType(models.Model):
    name = models.CharField(max_length=50)

    def str(self):
        return self.name


# 11
class Invoice(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    total = models.FloatField()

    def str(self):
        return str(self.total)


# 12
class Reservation(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    date = models.DateField()

    def str(self):
        return f"{self.customer} - {self.room}"