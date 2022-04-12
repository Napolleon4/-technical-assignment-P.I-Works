#usr/bin/python
 
import pandas as pd

df = pd.read_csv('country_vaccination_stats.csv')
data = df.fillna(value = {'daily_vaccinations': 0})
print(data) 
 