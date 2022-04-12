
from platform import python_branch



import pandas as pd 
import matplotlib.pyplot as plt

%matplotlib inline

data=pd.read_csv("dataset.csv")


plt.plot(data.feature_1,data.isVirus,color="red")
plt.plot(data.feature_2,data.isVirus,color="blue")
plt.plot(data.feature_3,data.isVirus,color="yellow")
plt.plot(data.feature_4,data.İsvirus,color="green")
plt.show()