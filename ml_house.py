import pandas
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error

#first file as testing data
file = 'C:\\Users\\djng4\\Desktop\\test.csv'

#pandas to read data into dataframe
data = pandas.read_csv(file)
data.columns
data.describe()
#data = data.dropna(axis=0)
y = data.Cost #predict y value 
features = ['Room numbers','Size','Yard']
x = data[features] #x value features

#decison tree model
model = DecisionTreeRegressor(random_state=1)

#fit the model to the data (compare)
model.fit(x,y)

#print model feature data
print(x.head())

#predict values
print("The predictions are")
print(model.predict(x.head()))
print(data.head())

#find mean absolute error (should be 0.0 here)
predicted_cost = model.predict(x)
print("The 2nd mean absolute error MAE is: ")
print(mean_absolute_error(y, predicted_cost))


#pandas to read live data into dataframe
file = 'C:\\Users\\djng4\\Desktop\\test1.csv'
data = pandas.read_csv(file)
data.columns
data.describe()
#data = data.dropna(axis=0)
y = data.Cost  #predict y value 
features = ['Room numbers','Size','Yard']
x = data[features]  #x value features

#predict values
print("The 2nd predictions are")
print(model.predict(x.head()))

#Find MAE mean error value (the closer to 0.0 the better)
print("The 2nd mean absolute error MAE is: ")
print(mean_absolute_error(y, predicted_cost))

