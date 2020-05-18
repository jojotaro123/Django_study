from django.urls import path
from . import views



urlpatterns = [
    path('bookinsert/',views.BookInsert.as_view())

]