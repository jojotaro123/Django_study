from django.urls import path
from . import views



urlpatterns = [
    path('booktest/',views.BookInsert.as_view())

]