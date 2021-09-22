from django.urls import path

from . import views


urlpatterns = [
    path('', views.htmlElement, name="basehtml"), # my-domain.com/mainapp
    path('<slug:item_id>', views.item_details, name="detail"), # my-domain.com/mainapp/dynamic-item-title
    path('<slug:item_id>/booking', views.booking_success, name="booking-success"),
]