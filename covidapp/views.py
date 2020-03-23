from django.shortcuts import render
from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup
import json



# Create your views here.
def home(request):
    return render(request,'covidapp/home.html')

def stats(request):
    url = 'https://www.covidout.in'
    page = requests.get(url)
    soup_obj = BeautifulSoup(page.content,'html.parser')
    output = soup_obj.findAll('h2',{'class':'case'})

    numbers = []

    for i in output:
        numbers.append(i.text)

    Confirmed_cases = numbers[0]
    Hospitalized_cases = numbers[1]
    Intensive_care_cases = numbers[2]
    Recovered_cases = numbers[3]
    Deaths = numbers[4]

    for i in range(0,len(numbers)):
        numbers[i] = int(numbers[i])

    return render(request,'covidapp/stats.html',{'Confirmed_cases':Confirmed_cases,'Hospitalized_cases':Hospitalized_cases,'Intensive_care_cases':Intensive_care_cases,'Recovered_cases':Recovered_cases,'Deaths':Deaths})

def instats(request):
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
    return render(request,{'China_df':China_df})
