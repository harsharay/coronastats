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

    state_1 = [stats_df.iloc[0][0],stats_df.iloc[0][1],stats_df.iloc[0][2],stats_df.iloc[0][3],stats_df.iloc[0][4]]
    state_2 = [stats_df.iloc[1][0],stats_df.iloc[1][1],stats_df.iloc[1][2],stats_df.iloc[1][3],stats_df.iloc[1][4]]
    state_3 = [stats_df.iloc[2][0],stats_df.iloc[2][1],stats_df.iloc[2][2],stats_df.iloc[2][3],stats_df.iloc[2][4]]
    state_4 = [stats_df.iloc[3][0],stats_df.iloc[3][1],stats_df.iloc[3][2],stats_df.iloc[3][3],stats_df.iloc[3][4]]
    state_5 = [stats_df.iloc[4][0],stats_df.iloc[4][1],stats_df.iloc[4][2],stats_df.iloc[4][3],stats_df.iloc[4][4]]
    state_6 = [stats_df.iloc[5][0],stats_df.iloc[5][1],stats_df.iloc[5][2],stats_df.iloc[5][3],stats_df.iloc[5][4]]
    state_7 = [stats_df.iloc[6][0],stats_df.iloc[6][1],stats_df.iloc[6][2],stats_df.iloc[6][3],stats_df.iloc[6][4]]
    state_8 = [stats_df.iloc[7][0],stats_df.iloc[7][1],stats_df.iloc[7][2],stats_df.iloc[7][3],stats_df.iloc[7][4]]
    state_9 = [stats_df.iloc[8][0],stats_df.iloc[8][1],stats_df.iloc[8][2],stats_df.iloc[8][3],stats_df.iloc[8][4]]
    state_10 = [stats_df.iloc[9][0],stats_df.iloc[9][1],stats_df.iloc[9][2],stats_df.iloc[9][3],stats_df.iloc[9][4]]
    state_11 = [stats_df.iloc[10][0],stats_df.iloc[10][1],stats_df.iloc[10][2],stats_df.iloc[10][3],stats_df.iloc[10][4]]
    state_12 = [stats_df.iloc[11][0],stats_df.iloc[11][1],stats_df.iloc[11][2],stats_df.iloc[11][3],stats_df.iloc[11][4]]
    state_13 = [stats_df.iloc[12][0],stats_df.iloc[12][1],stats_df.iloc[12][2],stats_df.iloc[12][3],stats_df.iloc[12][4]]
    state_14 = [stats_df.iloc[13][0],stats_df.iloc[13][1],stats_df.iloc[13][2],stats_df.iloc[13][3],stats_df.iloc[13][4]]
    state_15 = [stats_df.iloc[14][0],stats_df.iloc[14][1],stats_df.iloc[14][2],stats_df.iloc[14][3],stats_df.iloc[14][4]]
    state_16 = [stats_df.iloc[15][0],stats_df.iloc[15][1],stats_df.iloc[15][2],stats_df.iloc[15][3],stats_df.iloc[15][4]]
    state_17 = [stats_df.iloc[16][0],stats_df.iloc[16][1],stats_df.iloc[16][2],stats_df.iloc[16][3],stats_df.iloc[16][4]]
    state_18 = [stats_df.iloc[17][0],stats_df.iloc[17][1],stats_df.iloc[17][2],stats_df.iloc[17][3],stats_df.iloc[17][4]]
    state_19 = [stats_df.iloc[18][0],stats_df.iloc[18][1],stats_df.iloc[18][2],stats_df.iloc[18][3],stats_df.iloc[18][4]]
    state_20 = [stats_df.iloc[19][0],stats_df.iloc[19][1],stats_df.iloc[19][2],stats_df.iloc[19][3],stats_df.iloc[19][4]]
    state_21 = [stats_df.iloc[21][0],stats_df.iloc[21][1],stats_df.iloc[20][2],stats_df.iloc[20][3],stats_df.iloc[20][4]]
    state_22 = [stats_df.iloc[20][0],stats_df.iloc[20][1],stats_df.iloc[21][2],stats_df.iloc[21][3],stats_df.iloc[21][4]]
    state_23 = [stats_df.iloc[22][0],stats_df.iloc[22][1],stats_df.iloc[22][2],stats_df.iloc[22][3],stats_df.iloc[22][4]]
    state_24 = [stats_df.iloc[23][0],stats_df.iloc[23][1],stats_df.iloc[23][2],stats_df.iloc[23][3],stats_df.iloc[23][4]]
    state_25 = [stats_df.iloc[24][0],stats_df.iloc[24][1],stats_df.iloc[24][2],stats_df.iloc[24][3],stats_df.iloc[24][4]]
    state_26 = [stats_df.iloc[25][0],stats_df.iloc[25][1],stats_df.iloc[25][2],stats_df.iloc[25][3],stats_df.iloc[25][4]]
    state_27 = [stats_df.iloc[26][0],stats_df.iloc[26][1],stats_df.iloc[26][2],stats_df.iloc[26][3],stats_df.iloc[26][4]]
    state_28 = [stats_df.iloc[27][0],stats_df.iloc[27][1],stats_df.iloc[27][2],stats_df.iloc[27][3],stats_df.iloc[27][4]]
    state_29 = [stats_df.iloc[28][0],stats_df.iloc[28][1],stats_df.iloc[28][2],stats_df.iloc[28][3],stats_df.iloc[28][4]]
    state_30 = [stats_df.iloc[29][0],stats_df.iloc[29][1],stats_df.iloc[29][2],stats_df.iloc[29][3],stats_df.iloc[29][4]]
    state_31 = [stats_df.iloc[30][0],stats_df.iloc[30][1],stats_df.iloc[30][2],stats_df.iloc[30][3],stats_df.iloc[30][4]]
    state_32 = [stats_df.iloc[31][0],stats_df.iloc[31][1],stats_df.iloc[31][2],stats_df.iloc[31][3],stats_df.iloc[31][4]]
    state_33 = [stats_df.iloc[32][0],stats_df.iloc[32][1],stats_df.iloc[32][2],stats_df.iloc[32][3],stats_df.iloc[1][4]]
    state_34 = [stats_df.iloc[33][0],stats_df.iloc[33][1],stats_df.iloc[33][2],stats_df.iloc[33][3],stats_df.iloc[1][4]]
    state_35 = [stats_df.iloc[34][0],stats_df.iloc[34][1],stats_df.iloc[34][2],stats_df.iloc[34][3],stats_df.iloc[34][4]]
    state_36 = [stats_df.iloc[35][0],stats_df.iloc[35][1],stats_df.iloc[35][2],stats_df.iloc[35][3],stats_df.iloc[35][4]]
    state_37 = [stats_df.iloc[36][0],stats_df.iloc[36][1],stats_df.iloc[36][2],stats_df.iloc[36][3],stats_df.iloc[36][4]]
    return render(request,'covidapp/statesdata.html', {'state_1_name':state_1[0],'state_1_c':state_1[1],'state_1_r':state_1[2],'state_1_d':state_1[3],'state_1_a':state_1[4],
                                                       'state_2_name':state_2[0],'state_2_c':state_2[1],'state_2_r':state_2[2],'state_2_d':state_2[3],'state_2_a':state_2[4],
                                                       'state_3_name':state_3[0],'state_3_c':state_3[1],'state_3_r':state_3[2],'state_3_d':state_3[3],'state_3_a':state_3[4],
                                                       'state_4_name':state_4[0],'state_4_c':state_4[1],'state_4_r':state_4[2],'state_4_d':state_4[3],'state_4_a':state_4[4],
                                                       'state_5_name':state_5[0],'state_5_c':state_5[1],'state_5_r':state_5[2],'state_5_d':state_5[3],'state_5_a':state_5[4],
                                                       'state_6_name':state_6[0],'state_6_c':state_6[1],'state_6_r':state_6[2],'state_6_d':state_6[3],'state_6_a':state_6[4],
                                                       'state_7_name':state_7[0],'state_7_c':state_7[1],'state_7_r':state_7[2],'state_7_d':state_7[3],'state_7_a':state_7[4],
                                                       'state_8_name':state_8[0],'state_8_c':state_8[1],'state_8_r':state_8[2],'state_8_d':state_8[3],'state_8_a':state_8[4],
                                                       'state_9_name':state_9[0],'state_9_c':state_9[1],'state_9_r':state_9[2],'state_9_d':state_9[3],'state_9_a':state_9[4],
                                                       'state_10_name':state_10[0],'state_10_c':state_10[1],'state_10_r':state_10[2],'state_10_d':state_10[3],'state_10_a':state_10[4],
                                                       'state_11_name':state_11[0],'state_11_c':state_11[1],'state_11_r':state_11[2],'state_11_d':state_11[3],'state_10_a':state_11[4],
                                                       'state_12_name':state_12[0],'state_12_c':state_12[1],'state_12_r':state_12[2],'state_12_d':state_12[3],'state_12_a':state_12[4],
                                                       'state_13_name':state_13[0],'state_13_c':state_13[1],'state_13_r':state_13[2],'state_13_d':state_13[3],'state_13_a':state_13[4],
                                                       'state_14_name':state_14[0],'state_14_c':state_14[1],'state_14_r':state_14[2],'state_14_d':state_14[3],'state_14_a':state_14[4],
                                                       'state_15_name':state_15[0],'state_15_c':state_15[1],'state_15_r':state_15[2],'state_15_d':state_15[3],'state_15_a':state_15[4],
                                                       'state_16_name':state_16[0],'state_16_c':state_16[1],'state_16_r':state_16[2],'state_16_d':state_16[3],'state_16_a':state_16[4],
                                                       'state_17_name':state_17[0],'state_17_c':state_17[1],'state_17_r':state_17[2],'state_17_d':state_17[3],'state_17_a':state_17[4],
                                                       'state_18_name':state_18[0],'state_18_c':state_18[1],'state_18_r':state_18[2],'state_18_d':state_18[3],'state_18_a':state_18[4],
                                                       'state_19_name':state_19[0],'state_19_c':state_19[1],'state_19_r':state_19[2],'state_19_d':state_19[3],'state_19_a':state_19[4],
                                                       'state_20_name':state_20[0],'state_20_c':state_20[1],'state_20_r':state_20[2],'state_20_d':state_20[3],'state_20_a':state_20[4],
                                                       'state_21_name':state_21[0],'state_21_c':state_21[1],'state_21_r':state_10[2],'state_21_d':state_21[3],'state_21_a':state_21[4],
                                                       'state_22_name':state_22[0],'state_22_c':state_22[1],'state_22_r':state_22[2],'state_22_d':state_22[3],'state_22_a':state_22[4],
                                                       'state_23_name':state_23[0],'state_23_c':state_23[1],'state_23_r':state_23[2],'state_23_d':state_23[3],'state_23_a':state_23[4],
                                                       'state_24_name':state_24[0],'state_24_c':state_24[1],'state_24_r':state_24[2],'state_24_d':state_24[3],'state_24_a':state_24[4],
                                                       'state_25_name':state_25[0],'state_25_c':state_25[1],'state_25_r':state_25[2],'state_25_d':state_25[3],'state_25_a':state_25[4],
                                                       'state_26_name':state_26[0],'state_26_c':state_26[1],'state_26_r':state_26[2],'state_26_d':state_26[3],'state_26_a':state_26[4],
                                                       'state_27_name':state_27[0],'state_27_c':state_27[1],'state_27_r':state_27[2],'state_27_d':state_27[3],'state_27_a':state_27[4],
                                                       'state_28_name':state_28[0],'state_28_c':state_28[1],'state_28_r':state_28[2],'state_28_d':state_28[3],'state_28_a':state_28[4],
                                                       'state_29_name':state_29[0],'state_29_c':state_29[1],'state_29_r':state_29[2],'state_29_d':state_29[3],'state_29_a':state_29[4],
                                                       'state_30_name':state_30[0],'state_30_c':state_30[1],'state_30_r':state_30[2],'state_30_d':state_30[3],'state_30_a':state_30[4],
                                                       'state_31_name':state_31[0],'state_31_c':state_31[1],'state_31_r':state_31[2],'state_31_d':state_31[3],'state_31_a':state_31[4],
                                                       'state_32_name':state_32[0],'state_32_c':state_32[1],'state_32_r':state_32[2],'state_32_d':state_32[3],'state_32_a':state_32[4],
                                                       'state_33_name':state_33[0],'state_33_c':state_33[1],'state_33_r':state_33[2],'state_33_d':state_33[3],'state_33_a':state_33[4],
                                                       'state_34_name':state_34[0],'state_34_c':state_34[1],'state_34_r':state_34[2],'state_34_d':state_34[3],'state_34_a':state_34[4],
                                                       'state_35_name':state_35[0],'state_35_c':state_35[1],'state_35_r':state_35[2],'state_35_d':state_35[3],'state_35_a':state_35[4],
                                                       'state_36_name':state_36[0],'state_36_c':state_36[1],'state_36_r':state_36[2],'state_36_d':state_36[3],'state_36_a':state_36[4],
                                                       'state_37_name':state_37[0],'state_37_c':state_37[1],'state_37_r':state_37[2],'state_37_d':state_37[3],'state_37_a':state_37[4]})
