from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('rooms', RoomViewSet)
router.register('customers', CustomerViewSet)
router.register('bookings', BookingViewSet)
router.register('foods', FoodViewSet)
router.register('orders', OrderViewSet)
router.register('staff', StaffViewSet)
router.register('services', ServiceViewSet)
router.register('payments', PaymentViewSet)
router.register('reviews', ReviewViewSet)
router.register('roomtypes', RoomTypeViewSet)
router.register('invoices', InvoiceViewSet)
router.register('reservations', ReservationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]