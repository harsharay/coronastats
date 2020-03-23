from django.shortcuts import render
from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup
import json
import pandas as pd



# Create your views here.
def home(request):
    return render(request,'covidapp/home.html')

def stats(request):
    return render(request, 'covidapp/stats.html')


def intstats(request):
    url = "https://covid-19-coronavirus-statistics.p.rapidapi.com/v1/stats"
    params = {'country':'China'}
    headers = {
    'x-rapidapi-host': "covid-19-coronavirus-statistics.p.rapidapi.com",
    'x-rapidapi-key': "2a3b15c6f1mshe3a9940adbcd05dp19ab89jsna95e11818f1f"
    }
    response = requests.get(url, params=params, headers=headers)
    test = response.json()
    final = test['data']['covid19Stats']
    Provinces_china = []
    for i in final:
        Provinces_china.append(i['province'])


    Confirmed_china = []
    for i in final:
        Confirmed_china.append(i['confirmed'])
    Total_confirmed_china = sum(Confirmed_china)


    Deaths_china = []
    for i in final:
        Deaths_china.append(i['deaths'])
    Total_deaths_china = sum(Deaths_china)

    Recovered_china = []
    for i in final:
        Recovered_china.append(i['recovered'])
    Total_recovered_china = sum(Recovered_china)

    China_df = pd.DataFrame(list(zip(Provinces_china,Confirmed_china,Deaths_china,Recovered_china)))
    return render(request,'covidapp/intstats.html',{'Confirmed_China':Total_confirmed_china,'Deaths_China':Total_deaths_china,'Recovered_China':Total_recovered_china})
