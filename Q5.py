#usr/bin/python
 
import pandas as pd

df = pd.read_csv('country_vaccination_stats.csv')
data = df.fillna(value = {'daily_vaccinations': 0}).groupby(['country']).median().sort_values(['daily_vaccinations'], ascending=False).head(3)
print(data) 
 