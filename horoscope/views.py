from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

#
# def leo(request):
#     return HttpResponse(' Zodiac sign - leo')
#
#
# def scorpio(request):
#     return HttpResponse(' Zodiac sign - scorpio')

zodiac_dict = {
    'aries': 'Aries - <br>First zodiac sign, planet Mars (21 March - 20 April).',
    'taurus': 'Taurus - <br>Second zodiac sign, planet Venus (21 April - 21 May).',
    'gemini': 'Gemini - <br>Third zodiac sign, planet Mercury (2 2May - 21 June).',
    'cancer': 'Cancer - <br>Forth zodiac sign, Moon (22 June - 2 July).',
    'leo': ' Leo - <br>Fifth  zodiac sign, planet Sun (23 July - 21 August).',
    'virgo': 'Virgo - <br>Sixth zodiac sign, planet Mercury (22 August - 22 September).',
    'libra': 'Libra - <br>Seventh zodiac sign, planet Venus (24 September - 23 October).',
    'scorpio': 'Scorpio - <br>Eighth zodiac sign, planet Mars (24 October - 22 November).',
    'sagittarius': 'Sagittarius - <br>Ninth zodiac sign, planet Jupiter (23 November - 22 December).',
    'capricorn': 'Capricorn - <br>Tenth zodiac sign, planet Saturn (23 December - 20 January).',
    'aquarius': 'Aquarius - <br>Eleventh zodiac sign, planets Uran and Saturn (21 January - 19 February).',
    'pisces': 'Pisces - <br>Twelfth zodiac sign, planet Jupiter (20 February - 20 March).',
}


def get_info_about_sign_zodiac(request, sign_zodiac: str):
    description = zodiac_dict.get(sign_zodiac, None)
    if description:
        return HttpResponse(description)
    else:
        return HttpResponseNotFound(f'Wrong zodiac sign - {sign_zodiac}...')


def get_info_about_sign_zodiac_by_number(request, sign_zodiac: int):
    zodiacs = list(zodiac_dict)
    if sign_zodiac > len(zodiacs):
        return HttpResponseNotFound(f'Wrong zodiac sign number - {sign_zodiac}...')
    name_zodiac = zodiacs[sign_zodiac-1]
    return HttpResponseRedirect(f'/horoscope/{name_zodiac}')
