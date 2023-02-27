from django.shortcuts import render
import json
import urllib.request

# Create your views here.

def index(request):
    if request.method=='POST':
        city=request.POST['city']
        
        res=urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='+ city + '&appid=bb03ca9ad5f184fe6651fbeee5d4fd8e').read()  #sending a reqeust to the openmapp
        
        json_data=json.loads(res)           #getting the results from our api and we will used a dic for easy rendering
        
        data={
            "country_code": str(json_data['sys']['country']), 
            "coordinates": str(json_data['coord']['lon']) + ' ' + str(json_data['coord']['lat']),       #getting the longitued and latitude
            "temp": str(json_data['main']['temp']) + 'k',
            "pressure":str(json_data['main']['pressure']),
            "humidity": str(json_data['main']['humidity']),

        }
    else:
        data={}
        
    return render(request, 'index.html', data)