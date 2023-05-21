from django.urls import path
from . import views


urlpatterns = [
    
    #path('bookings/', views.BookingView.as_view(), name='booking'),
    path('menu/', views.MenuItemView.as_view(), name="menu"),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('bookings/', views.BookingViewSet.as_view(), name='booking')
]
