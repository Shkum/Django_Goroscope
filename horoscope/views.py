from django.shortcuts import render

from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


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


def index(request):
    zodiacs = list(zodiac_dict)
    context = {
        'zodiacs': zodiacs,
        'zodiac_dict': zodiac_dict
    }
    return render(request, 'horoscope/index.html', context=context)


def get_info_about_sign_zodiac(request, sign_zodiac: str):

    description = zodiac_dict.get(sign_zodiac)
    data = {
        'description_zodiac': description,
        'sign': sign_zodiac
    }
    return render(request, 'horoscope/info_zodiac.html', context=data)


def get_info_about_sign_zodiac_by_number(request, sign_zodiac: int):
    zodiacs = list(zodiac_dict)
    if sign_zodiac > len(zodiacs):
        return HttpResponseNotFound(f'Wrong zodiac sign number - {sign_zodiac}...')
    name_zodiac = zodiacs[sign_zodiac - 1]
    redirect_url = reverse('horoscope_name', args=[name_zodiac])  # create redirect path using path from urls.py
    return HttpResponseRedirect(redirect_url)
