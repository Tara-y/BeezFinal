from django.urls import path
from .views import *

urlpatterns = [
    path('register/',register, name="register"),
    path('login/',userlogin,name="login"),
    path('logout/',userlogout,name="logout"),
    path('addReview/',addReview, name="addReview"),
    path('myReviews/',myReviews, name="myReviews")
]

