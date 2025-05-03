from django.shortcuts import render
import requests 
import json

# Create your views here.
def index(request):
    api = 'b27c6a546b6a0dc3a7843b7914915183'
    result = {}
    if request.method == 'POST':
        city = request.POST['city']
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}&units=metric"
        response = requests.get(url)
        print(response.json())
        result = response.json()


    return render(request, 'index.html', {"data": result })