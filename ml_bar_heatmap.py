import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns
print("Setup Complete")

file = 'C://Users//djng4//Desktop/flight_delays.csv'

data1 = pd.read_csv(file, index_col="Month")

data1.head()

#build bar graph
plt.figure(figsize=(10,6))
plt.title("Flight times")
sns.barplot(x=data1.index,y=data1['B6'])
plt.xlabel("Month")
plt.ylabel("Time")

#build heatmap for all data
sns.heatmap(data=data1, annot=True)