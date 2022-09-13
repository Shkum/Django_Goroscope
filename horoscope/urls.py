from django.urls import path, register_converter
from . import views, converters

register_converter(converters.FourDigitConverter, 'yyyy')
register_converter(converters.FloatConverter, 'my_float')
register_converter(converters.DateConverter, 'my_date')


urlpatterns = [
    path('', views.index, name='horoscope_index'),
    path('<int:sign_zodiac>/', views.get_info_about_sign_zodiac_by_number),
    path('<str:sign_zodiac>/', views.get_info_about_sign_zodiac, name='horoscope_name'),
]
