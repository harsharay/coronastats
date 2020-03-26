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
    url = "https://api.rootnet.in/covid19-in/unofficial/covid19india.org/statewise"
    response = requests.get(url)
    final_response = response.json()
    confirmed_cases_india = final_response['data']['total']['confirmed']

    Deaths_India=final_response['data']['total']['deaths']

    Active_Cases_India = final_response['data']['total']['active']

    Recovered_India =final_response['data']['total']['recovered']


    #India_df = pd.DataFrame(list(zip(Provinces_china,Confirmed_china,Deaths_china,Recovered_china)))
    return render(request,'covidapp/stats.html',{'Confirmed_cases_India':confirmed_cases_india,'Deaths_india':Deaths_India,'Active_cases_india':Active_Cases_India,'Recovered_cases_india':Recovered_India})


def intstats(request):
    def country_stat(country_1):
        url='https://covid-193.p.rapidapi.com/statistics'
        headers = {
        'x-rapidapi-host': "covid-193.p.rapidapi.com",
        'x-rapidapi-key': "2a3b15c6f1mshe3a9940adbcd05dp19ab89jsna95e11818f1f"
        }
        response = requests.get(url,params={"country":country_1},headers=headers)
        resp_2 = response.json()
        final_resp = resp_2['response']
        output = final_resp[0]
        return output
    #China data
    final_response_china = country_stat("China")
    Deaths_china=final_response_china['deaths']

    Cases_China = final_response_china['cases']

    Recovered_China =Cases_China['recovered']
    #------------------------------------------------------------
    #Italy Data
    final_response_italy = country_stat('Italy')
    Deaths_italy=final_response_italy['deaths']

    Cases_italy = final_response_italy['cases']

    Recovered_italy =Cases_italy['recovered']
    #------------------------------------------------------------
    #USA Data
    final_response_usa = country_stat('USA')
    Deaths_usa=final_response_usa['deaths']

    Cases_usa = final_response_usa['cases']

    Recovered_usa =Cases_usa['recovered']
    #------------------------------------------------------------
    #Spain Data
    final_response_spain = country_stat('Spain')
    Deaths_spain=final_response_spain['deaths']

    Cases_spain = final_response_spain['cases']

    Recovered_spain =Cases_spain['recovered']

    return render(request,'covidapp/intstats.html',{'Total_cases_China':Cases_China['total'],'Active_cases':Cases_China['active'],'Critical_cases':Cases_China['critical'],'new_cases_china':Cases_China['new'],'New_deaths_China_today':Deaths_china['new'],'Total_deaths_China':Deaths_china['total'],'Recovered_china':Recovered_China,'Total_cases_italy':Cases_italy['total'],'Active_cases_italy':Cases_italy['active'],'Critical_cases_taly':Cases_italy['critical'],'new_cases_italy':Cases_italy['new'],'New_deaths_italy_today':Deaths_italy['new'],'Total_deaths_italy':Deaths_italy['total'],'Recovered_italy':Recovered_italy,'Total_cases_usa':Cases_usa['total'],'Active_cases_usa':Cases_usa['active'],'Critical_cases_usa':Cases_usa['critical'],'new_cases_usa':Cases_usa['new'],'New_deaths_usa_today':Deaths_usa['new'],'Total_deaths_usa':Deaths_usa['total'],'Recovered_usa':Recovered_usa,'Total_cases_spain':Cases_spain['total'],'Active_cases_spain':Cases_spain['active'],'Critical_cases_spain':Cases_spain['critical'],'new_cases_spain':Cases_spain['new'],'New_deaths_spain_today':Deaths_spain['new'],'Total_deaths_spain':Deaths_spain['total'],'Recovered_spain':Recovered_spain})


def helpline(request):
    return render(request, 'covidapp/helplines.html')

def statesdata(request):
    url = "https://api.rootnet.in/covid19-in/unofficial/covid19india.org/statewise"
    response = requests.get(url)
    final_response = response.json()
    states_data = final_response['data']['statewise']
    states=[]
    confirmed_cases = []
    recovered_cases = []
    deaths =[]
    active = []

    for i in states_data:
        states.append(i['state'])

    for i in states_data:
        confirmed_cases.append(i['confirmed'])

    for i in states_data:
        recovered_cases.append(i['recovered'])

    for i in states_data:
        deaths.append(i['deaths'])

    for i in states_data:
        active.append(i['active'])

    stats_df = pd.DataFrame(list(zip(states,confirmed_cases,recovered_cases,deaths,active)))

    stats_df.columns = ['states','confirmed','recovered','deaths','active']

    Maharashtra = stats_df.iloc[0]
    Kerala = stats_df.iloc[1]
    Karnataka = stats_df.iloc[2]
    Telangana = stats_df.iloc[3]
    Gujarat = stats_df.iloc[4]
    Uttar_Pradesh = stats_df.iloc[5]
    Rajasthan = stats_df.iloc[6]
    Delhi = stats_df.iloc[7]
    Haryana = stats_df.iloc[8]
    Punjab = stats_df.iloc[9]
    Tamil_Nadu = stats_df.iloc[10]
    Madhya_Pradesh = stats_df.iloc[11]
    Ladakh = stats_df.iloc[12]
    Jammu_and_Kashmir = stats_df.iloc[13]
    Andhra_Pradesh = stats_df.iloc[14]
    West_Bengal = stats_df.iloc[15]
    Chandigarh = stats_df.iloc[16]
    Uttarakand = stats_df.iloc[17]
    Bihar = stats_df.iloc[18]
    Himachal_Pradesh = stats_df.iloc[19]
    Chhattisgarh = stats_df.iloc[20]
    Goa = stats_df.iloc[21]
    Odisha = stats_df.iloc[22]
    Puducherry = stats_df.iloc[23]
    Manipur = stats_df.iloc[24]
    Mizoram = stats_df.iloc[25]
    Andaman_and_Nicobar_Islands = stats_df.iloc[26]
    Assam = stats_df.iloc[27]
    Meghalaya = stats_df.iloc[28]
    Tripura = stats_df.iloc[29]
    Arunachal_Pradesh = stats_df.iloc[30]
    Jharkand = stats_df.iloc[31]
    Nagaland = stats_df.iloc[32]
    Sikkim = stats_df.iloc[33]
    Dadra_and_Nagar_Haveli = stats_df.iloc[34]
    Damana_and_diu = stats_df.iloc[35]
    Lakshadweep = stats_df.iloc[36]
    return render(request,'covidapp/statesdata.html', {'Maharashtra_conf':Maharashtra[1],'Maharashtra_recov':Maharashtra[2],'Maharashtra_deaths':Maharashtra[3],'Maharashtra_active':Maharashtra[4],
                                                       'Kerala_conf':Kerala[1],'Kerala_recov':Kerala[2],'Kerala_deaths':Kerala[3],'Kerala_active':Kerala[4],
                                                       'Karnataka_conf':Karnataka[1],'Karnataka_recov':Karnataka[2],'Karnataka_deaths':Karnataka[3],'Karnataka_active':Karnataka[4],
                                                       'Telangana_conf':Telangana[1],'Telangana_recov':Telangana[2],'Telangana_deaths':Telangana[3],'Telangana_active':Telangana[4],
                                                       'Gujarat_conf':Gujarat[1],'Gujarat_recov':Gujarat[2],'Gujarat_deaths':Gujarat[3],'Gujarat_active':Gujarat[4],
                                                       'Uttar_Pradesh_conf':Uttar_Pradesh[1],'Uttar_Pradesh_recov':Uttar_Pradesh[2],'Uttar_Pradesh_deaths':Uttar_Pradesh[3],'Uttar_Pradesh_active':Uttar_Pradesh[4],
                                                       'Rajasthan_conf':Rajasthan[1],'Rajasthan_recov':Rajasthan[2],'Rajasthan_deaths':Rajasthan[3],'Rajasthan_active':Rajasthan[4],
                                                       'Delhi_conf':Delhi[1],'Delhi_recov':Delhi[2],'Delhi_deaths':Delhi[3],'Delhi_active':Delhi[4],
                                                       'Haryana_conf':Haryana[1],'Haryana_recov':Haryana[2],'Haryana_deaths':Haryana[3],'Haryana_active':Haryana[4],
                                                       'Punjab_conf':Punjab[1],'Punjab_recov':Punjab[2],'Punjab_deaths':Punjab[3],'Punjab_active':Punjab[4],
                                                       'Tamil_Nadu_conf':Tamil_Nadu[1],'Tamil_Nadu_recov':Tamil_Nadu[2],'Tamil_Nadu_deaths':Tamil_Nadu[3],'Tamil_Nadu_active':Tamil_Nadu[4],
                                                       'Madhya_Pradesh_conf':Madhya_Pradesh[1],'Madhya_Pradesh_recov':Madhya_Pradesh[2],'Madhya_Pradesh_deaths':Madhya_Pradesh[3],'Madhya_Pradesh_active':Madhya_Pradesh[4],
                                                       'Ladakh_conf':Ladakh[1],'Ladakh_recov':Ladakh[2],'Ladakh_deaths':Ladakh[3],'Ladakh_active':Ladakh[4],
                                                       'Jammu_and_Kashmir_conf':Jammu_and_Kashmir[1],'Jammu_and_Kashmir_recov':Jammu_and_Kashmir[2],'Jammu_and_Kashmir_deaths':Jammu_and_Kashmir[3],'Jammu_and_Kashmir_active':Jammu_and_Kashmir[4],
                                                       'Andhra_Pradesh_conf':Andhra_Pradesh[1],'Andhra_Pradesh_recov':Andhra_Pradesh[2],'Andhra_Pradesh_deaths':Andhra_Pradesh[3],'Andhra_Pradesh_active':Andhra_Pradesh[4],
                                                       'West_Bengal_conf':West_Bengal[1],'West_Bengal_recov':West_Bengal[2],'West_Bengal_deaths':West_Bengal[3],'West_Bengal_active':West_Bengal[4],
                                                       'Chandigarh_conf':Chandigarh[1],'Chandigarh_recov':Chandigarh[2],'Chandigarh_deaths':Chandigarh[3],'Chandigarh_active':Chandigarh[4],
                                                       'Uttarakand_conf':Uttarakand[1],'Uttarakand_recov':Uttarakand[2],'Uttarakand_deaths':Uttarakand[3],'Uttarakand_active':Uttarakand[4],
                                                       'Bihar_conf':Bihar[1],'Bihar_recov':Bihar[2],'Bihar_deaths':Bihar[3],'Bihar_active':Bihar[4],
                                                       'Himachal_Pradesh_conf':Himachal_Pradesh[1],'Himachal_Pradesh_recov':Himachal_Pradesh[2],'Himachal_Pradesh_deaths':Himachal_Pradesh[3],'Himachal_Pradesh_active':Himachal_Pradesh[4],
                                                       'Chhattisgarh_conf':Chhattisgarh[1],'Chhattisgarh_recov':Chhattisgarh[2],'Chhattisgarh_deaths':Chhattisgarh[3],'Chhattisgarh_active':Chhattisgarh[4],
                                                       'Goa_conf':Goa[1],'Goa_recov':Goa[2],'Goa_deaths':Goa[3],'Goa_active':Goa[4],
                                                       'Odisha_conf':Odisha[1],'Odisha_recov':Odisha[2],'Odisha_deaths':Odisha[3],'Odisha_active':Odisha[4],
                                                       'Puducherry_conf':Puducherry[1],'Puducherry_recov':Puducherry[2],'Puducherry_deaths':Puducherry[3],'Puducherry_active':Puducherry[4],
                                                       'Manipur_conf':Manipur[1],'Manipur_recov':Manipur[2],'Manipur_deaths':Manipur[3],'Manipur_active':Manipur[4],
                                                       'Mizoram_conf':Mizoram[1],'Mizoram_recov':Mizoram[2],'Mizoram_deaths':Mizoram[3],'Mizoram_active':Mizoram[4],
                                                       'Andaman_and_Nicobar_Islands_conf':Andaman_and_Nicobar_Islands[1],'Andaman_and_Nicobar_Islands_recov':Andaman_and_Nicobar_Islands[2],'Andaman_and_Nicobar_Islandsdeaths':Andaman_and_Nicobar_Islands[3],'Andaman_and_Nicobar_Islands_active':Andaman_and_Nicobar_Islands[4],
                                                       'Assam_conf':Assam[1],'Assam_recov':Assam[2],'Assam_deaths':Assam[3],'Assam_active':Assam[4],
                                                       'Meghalaya_conf':Meghalaya[1],'Meghalaya_recov':Meghalaya[2],'Meghalaya_deaths':Meghalaya[3],'Meghalaya_active':Meghalaya[4],
                                                       'Tripura_conf':Tripura[1],'Tripura_recov':Tripura[2],'Tripura_deaths':Tripura[3],'Tripura_active':Tripura[4],
                                                       'Arunachal_Pradesh_conf':Arunachal_Pradesh[1],'Arunachal_Pradesh_recov':Arunachal_Pradesh[2],'Arunachal_Pradesh_deaths':Arunachal_Pradesh[3],'Arunachal_Pradesh_active':Arunachal_Pradesh[4],
                                                       'Jharkand_conf':Jharkand[1],'Jharkand_recov':Jharkand[2],'Jharkand_deaths':Jharkand[3],'Jharkand_active':Jharkand[4],
                                                       'Nagaland_conf':Nagaland[1],'Nagaland_recov':Nagaland[2],'Nagaland_deaths':Nagaland[3],'Nagaland_active':Nagaland[4],
                                                       'Sikkim_conf':Sikkim[1],'Sikkim_recov':Sikkim[2],'Sikkim_deaths':Sikkim[3],'Sikkim_active':Sikkim[4],
                                                       'Dadra_and_Nagar_Haveli_conf':Dadra_and_Nagar_Haveli[1],'Dadra_and_Nagar_Haveli_recov':Dadra_and_Nagar_Haveli[2],'Dadra_and_Nagar_Haveli_deaths':Dadra_and_Nagar_Haveli[3],'Dadra_and_Nagar_Haveli_active':Dadra_and_Nagar_Haveli[4],
                                                       'Damana_and_diu_conf':Damana_and_diu[1],'Damana_and_diu_recov':Damana_and_diu[2],'Damana_and_diu_deaths':Damana_and_diu[3],'Damana_and_diu_active':Damana_and_diu[4],
                                                       'Lakshadweep_conf':Lakshadweep[1],'Lakshadweep_recov':Lakshadweep[2],'Lakshadweep_deaths':Lakshadweep[3],'Lakshadweep_active':Lakshadweep[4],})
