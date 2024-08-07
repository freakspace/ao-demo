from django.urls import path

from . import views

app_name = "orders"

urlpatterns = [
    path("", views.OrderListView.as_view(), name="order_list"),
    path("<slug:pk>/", views.OrderDetailView.as_view(), name="order_detail"),
]
