from django.http import HttpResponse
from django.shortcuts import render
import requests

def index(request):
    return render(request,'index.html')


def get_weather(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        api_key = 'f890928e3bd17a316806634a4d5b6d1a'
        api_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}'
        response = requests.get(api_url)
        data = response.json()
        return render(request, 'climate.html', {'data': data, 'city': city})

# def climatefun(request):
#     if request.method == 'POST':
#         city = request.POST.get('city')
#     response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=f890928e3bd17a316806634a4d5b6d1a')
#     data = response.json()
#     return render(request,'climate.html',{'data':data},{'city':city})
