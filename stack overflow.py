import pandas as pd
from collections import Counter
import numpy as np
from matplotlib import pyplot as plt
import csv
plt.style.use('fivethirtyeight')

data=pd.read_csv('Downloads/newdata/survey_results_public.csv')

pd.set_option('display.max_column',80)
data.head(50)

ids=data['Respondent']

language_res=data['LanguageWorkedWith'].dropna()


language_counter=Counter()
for response in language_res:
    language_counter.update(response.split(';'))
print(language_counter)

languages=list()
popularity=list()

for item in language_counter.most_common(15):
    languages.append(item[0])
    popularity.append(item[1])
print(languages)

languages.reverse()
popularity.reverse()

plt.xlabel('popularity')
plt.ylabel('languages')
plt.barh(languages,popularity,label='Popular languages')
plt.tight_layout()

fil=data['Country']=='India'

India_lan=data.loc[fil]

Inln_counter=Counter()

for res in India_lan['LanguageWorkedWith'].dropna():
    Inln_counter.update(res.split(';'))
print(Inln_counter)

in_languages=list()
in_popularity=list()

for item in Inln_counter.most_common(15):
    in_languages.append(item[0])
    in_popularity.append(item[1])
print(in_languages)

in_languages.reverse()
in_popularity.reverse()

plt.xlabel('popularity')
plt.ylabel('languages')
plt.barh(languages,popularity,label='Popular Indian language ')
plt.tight_layout()

y_avgSal=list()
India_dev_avgsal=data.loc[data['Country']=='India',['ConvertedComp']].dropna().mean()
y_avgSal.append(India_dev_avgsal)

US_dev_avgsal=data.loc[data['Country']=='United States',['ConvertedComp']].dropna().mean()
y_avgSal.append(US_dev_avgsal)
Germany_dev_avgsal=data.loc[data['Country']=='Germany',['ConvertedComp']].dropna().mean()
y_avgSal.append(Germany_dev_avgsal)
UK_dev_avgsal=data.loc[data['Country']=='United Kingdom',['ConvertedComp']].dropna().mean()
y_avgSal.append(UK_dev_avgsal)
France_dev_avgsal=data.loc[data['Country']=='France',['ConvertedComp']].dropna().mean()
y_avgSal.append(France_dev_avgsal)
spain_dev_avgsal=data.loc[data['Country']=='Spain',['ConvertedComp']].dropna().mean()
y_avgSal.append(spain_dev_avgsal)
Brazil_dev_avgsal=data.loc[data['Country']=='Brazil',['ConvertedComp']].dropna().mean()
y_avgSal.append(Brazil_dev_avgsal)

x_country=['India','US','Germany','UK','France','Spain','Brazil']

plt.xlabel('Country')
plt.ylabel('Salary')
plt.title('Avarage Salary of Various Country')
plt.plot(x_country,y_avgSal)

India_H=data.loc[data['Country']=='India']
In=India_H['Hobbyist'].value_counts().tolist()

Us_H=data.loc[data['Country']=='United States']
US=Us_H['Hobbyist'].value_counts().tolist()

Uk_H=data.loc[data['Country']=='United Kingdom']
UK=Uk_H['Hobbyist'].value_counts().tolist()

Germany_H=data.loc[data['Country']=='Germany']
Germany=Germany_H['Hobbyist'].value_counts().tolist()

France_H=data.loc[data['Country']=='France']
France=France_H['Hobbyist'].value_counts().tolist()

Brazil_H=data.loc[data['Country']=='Brazil']
Brazil=Brazil_H['Hobbyist'].value_counts().tolist()

country=['India','US','UK','Germany','France','Brazil']

hobbyist_dev=[In[0],US[0],UK[0],Germany[0],France[0],Brazil[0]]
nonhobbyist_dev=[In[1],US[1],UK[1],Germany[1],France[1],Brazil[1]]

width=0.25
plt.xlabel('Country')
plt.title('hobbyist and non-hobbyist dev. ')
plt.plot(country,hobbyist_dev,label='Hobbyist')
plt.plot(country,nonhobbyist_dev,label='Non-Hobbyist')
plt.legend()
