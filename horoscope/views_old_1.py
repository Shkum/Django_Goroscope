# Create your views here.
from dataclasses import dataclass

from django.shortcuts import render

from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

#
# def leo(request):
#     return HttpResponse(' Zodiac sign - leo')
#
#
# def scorpio(request):
#     return HttpResponse(' Zodiac sign - scorpio')

zodiac_dict = {
    'aries': 'Aries - First zodiac sign, planet Mars (21 March - 20 April).',
    'taurus': 'Taurus - Second zodiac sign, planet Venus (21 April - 21 May).',
    'gemini': 'Gemini - Third zodiac sign, planet Mercury (2 2May - 21 June).',
    'cancer': 'Cancer - Forth zodiac sign, Moon (22 June - 2 July).',
    'leo': ' Leo - Fifth  zodiac sign, planet Sun (23 July - 21 August).',
    'virgo': 'Virgo - Sixth zodiac sign, planet Mercury (22 August - 22 September).',
    'libra': 'Libra - Seventh zodiac sign, planet Venus (24 September - 23 October).',
    'scorpio': 'Scorpio - Eighth zodiac sign, planet Mars (24 October - 22 November).',
    'sagittarius': 'Sagittarius - Ninth zodiac sign, planet Jupiter (23 November - 22 December).',
    'capricorn': 'Capricorn - Tenth zodiac sign, planet Saturn (23 December - 20 January).',
    'aquarius': 'Aquarius - Eleventh zodiac sign, planets Uran and Saturn (21 January - 19 February).',
    'pisces': 'Pisces - Twelfth zodiac sign, planet Jupiter (20 February - 20 March).'
}

zodiac_elements = {"fire": ['aries', 'leo', 'sagittarius'],
                   'earth': ['taurus', 'virgo', 'capricorn'],
                   'air': ['gemini', 'libra', 'aquarius'],
                   'water': ['cancer', 'scorpio', 'pisces']}

zodiac_dates = {
    'aries': [80, 110],
    'taurus': [111, 141],
    'gemini': [142, 172],
    'cancer': [173, 203],
    'leo': [204, 233],
    'virgo': [234, 265],
    'libra': [267, 296],
    'scorpio': [297, 326],
    'sagittarius': [327, 356],
    'capricorn': [357, 20],
    'aquarius': [21, 50],
    'pisces': [51, 79],
}

months = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}


def index(request):
    zodiacs = list(zodiac_dict)
    # li_element += f'<li><a href="{redirect_path}">{sign.title()}</a></li>'
    context = {
        'zodiacs': zodiacs,
        'zodiac_dict': zodiac_dict
    }
    return render(request, 'horoscope/index.html', context=context)


@dataclass
class Person:
    name: str
    age: int

    def __str__(self):
        return f'This is {self.name}'


def get_info_about_sign_zodiac(request, sign_zodiac: str):
    # response = render_to_string('horoscope/info_zodiac.html')
    # return HttpResponse(response)
    description = zodiac_dict.get(sign_zodiac)
    data = {
        'description_zodiac': description,
        'my_int': 1111,
        'my_float': 111.5,
        'sign': sign_zodiac,
        'my_list': [1, 2, 3],
        'my_dict': {'name': 'Jack', 'age': 40},
        'my_class': Person('Will', 55),
        'value': [],
        'value_1': [],
        'value_2': [1, 2, 3]
    }
    return render(request, 'horoscope/info_zodiac.html', context=data)


# reverse - getting path from variable name from view
# from news import views
# path('archive/', views.archive, name='news-archive')
# from django.urls import reverse
# reverse('news-archive')
def get_info_about_sign_zodiac_by_number(request, sign_zodiac: int):
    zodiacs = list(zodiac_dict)
    if sign_zodiac > len(zodiacs):
        return HttpResponseNotFound(f'Wrong zodiac sign number - {sign_zodiac}...')
    name_zodiac = zodiacs[sign_zodiac - 1]
    redirect_url = reverse('horoscope_name', args=[name_zodiac])  # create redirect path using path from urls.py
    # return HttpResponseRedirect(f'/horoscope/{name_zodiac}')
    return HttpResponseRedirect(redirect_url)


def get_info_about_sign_zodiac_elements(request):
    li_element = ''
    for sign in zodiac_elements:
        redirect_path = reverse('element_name', args=[sign])
        li_element += f'<li><a href="{redirect_path}">{sign}</a></li>'
    response = f'''
    <ul>
    {li_element}
    </ul>
    '''
    return HttpResponse(response)


def get_info_about_sign_zodiac_by_elements(request, sign_element: str):
    li_element = ''
    for sign in zodiac_elements[sign_element]:
        redirect_path = reverse('horoscope_name', args=[sign])
        li_element += f'<li><a href="{redirect_path}">{sign}</a></li>'
    response = f'''
    <ul>
    {li_element}
    </ul>
    '''
    return HttpResponse(response)


def get_info_by_date(request, month, day):
    if month > 12 or day > months[month]:
        return HttpResponse('<h2>Wrong month or day number</h2>')
    else:
        days = 0
        for i in range(1, month):
            days += months[i]
        days += day
        for i in zodiac_dates:
            if zodiac_dates[i][1] >= days >= zodiac_dates[i][0]:
                return HttpResponse(f"<h2>{i.title()}</h2>")

    return HttpResponse("<h2>Capricorn</h2>")


def get_four_digits(request, dddd):
    return HttpResponse(f'<h2>Entered four digit number: {dddd}</h2>')


def get_float_number(request, v_float):
    return HttpResponse(f'<h2>You entered float number: {v_float}</h2>')


def get_entered_data(request, v_date):
    return HttpResponse(f'<h2>You entered date: {v_date}</h2>')
