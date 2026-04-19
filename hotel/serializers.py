from rest_framework import serializers
from .models import *

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = 'all'


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = 'all'


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = 'all'


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = 'all'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = 'all'


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = 'all'


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = 'all'


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = 'all'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'all'


class RoomTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomType
        fields = 'all'


class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = 'all'


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = 'all'