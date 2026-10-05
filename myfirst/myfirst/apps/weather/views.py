from django.shortcuts import render
import os

import requests

def weather_view(request):
    access_key = os.getenv('YANDEX_WEATHER_API_KEY', '')

    headers = {
        'X-Yandex-API-Key': access_key
    }

    response = requests.get(
        'https://api.weather.yandex.ru/v2/forecast?lat=43.3176&lon=45.6981',
        headers=headers
    )

    context = {}

    if response.status_code == 200:
        data = response.json()
        fact = data.get('fact', {})

        context = {
            "temp": fact.get('temp'),
            "feels_like": fact.get('feels_like'),
        }
    else:
        context = {
            "error": f"Ошибка запроса: {response.status_code}"
        }

    return render(request, 'weather.html', context)
