from django.shortcuts import render, HttpResponse
from django. shortcuts import render, HttpResponse
from django.conf import settings
import requests
import json


api_key = settings.GEO_API_KEY
api_url = 'https://ipgeolocation.abstractapi.com/v1/?api_key=' + api_key


def get_ip_geolocation_data(ip_address):
    # not using the incoming IP address for testing
    print(ip_address)
    response = requests.get(api_url)
    return response.content


def home(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    geolocation_json = get_ip_geolocation_data(ip)
    geolocation_data = json.loads(geolocation_json)
    country = geolocation_data['country']
    region = geolocation_data['region']
    city = geolocation_data['city']

    return HttpResponse("Welcome! Your IP address is: {} and you are visiting from {} in {}".format(ip, city, country))
