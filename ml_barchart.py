import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns
print("Setup Complete")

file = 'C://Users//DJNG4/Downloads/fifa.csv'

data1 = pd.read_csv(file, index_col="Date",parse_dates=True)

data1.head()

#build line graph
plt.figure(figsize=(10,6))
plt.title("FIFA Results")
sns.lineplot(data=data1['ESP'])
sns.lineplot(data=data1['ARG'])
plt.xlabel("Date")
plt.ylabel("Size")