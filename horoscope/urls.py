from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<int:sign_zodiac>/', views.get_info_about_sign_zodiac_by_number),
    path('<str:sign_zodiac>/', views.get_info_about_sign_zodiac, name='horoscope_name'),
    path('type', views.get_info_about_sign_zodiac_elements),
    path('type/<str:sign_element>', views.get_info_about_sign_zodiac_by_elements, name='element_name'),


    # path('leo/', views.leo),
    # path('scorpio/', views.scorpio),
]
