from django.urls import path
from .views import CoffeeList, CoffeeDetail

urlpatterns = [
  path("", CoffeeList.as_view(), name="coffee_list"),
  path("<int:pk>/", CoffeeDetail.as_view(), name="thing_detail"),
]