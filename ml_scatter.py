import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns
print("Setup Complete")
plt.figure(figsize=(10,6))
plt.title("Flight times")


file = 'C://Users//djng4//Downloads/insurance.csv'

data = pd.read_csv(file)

data.head()

#build graph
#sns.regplot(x=data['bmi'], y=data['charges'])
#sns.scatterplot(x=data['bmi'], y=data['charges'], hue=data['smoker'])
#sns.lmplot(x="bmi", y="charges", hue="smoker", data=data)
sns.stripplot(x=data['smoker'],
              y=data['charges'])  #or sns.swarmplot