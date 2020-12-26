import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns
print("Setup Complete")
plt.figure(figsize=(10,6))
plt.title("Graph Title")


file = 'C://Users//djng4//Downloads/iris.csv'

data = pd.read_csv(file)

data.head()

#histogram
#sns.distplot(a=data['Petal Length (cm)'], kde=False)

# KDE plot 
sns.kdeplot(data=data['Petal Length (cm)'], shade=True)