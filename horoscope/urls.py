from django.urls import path, register_converter
from . import views, converters

register_converter(converters.FourDigitConverter, 'yyyy')
register_converter(converters.FloatConverter, 'my_float')
register_converter(converters.DateConverter, 'my_date')


urlpatterns = [
    path('', views.index),
    path('<yyyy:dddd>', views.get_four_digits),
    path('<my_date:v_date>', views.get_entered_data),
    path('<int:sign_zodiac>/', views.get_info_about_sign_zodiac_by_number),

    path('<str:sign_zodiac>/', views.get_info_about_sign_zodiac, name='horoscope_name'),
    path('type', views.get_info_about_sign_zodiac_elements),
    path('type/<str:sign_element>', views.get_info_about_sign_zodiac_by_elements, name='element_name'),
    path('<my_float:v_float>', views.get_float_number),
    path('<int:month>/<int:day>', views.get_info_by_date)

    # path('leo/', views.leo),
    # path('scorpio/', views.scorpio),
]
