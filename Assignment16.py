import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score

def Advertise(tv_budget, radio_budget, newspaper_budget):

    data = pd.read_csv('advertising.csv')
    
    X = data[['TV', 'radio', 'newspaper']]
    Y = data['sales']
    
    print("Data shape:", X.shape, Y.shape)
    
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=42)
    
    model = LinearRegression()
    
    model.fit(X_train, Y_train)
    
    Y_pred = model.predict(X_test)
    
    mean =  mean_squared_error(Y_test, Y_pred)
    print("Mean Squared Error:",mean)

    r2 = r2_score(Y_test,Y_pred)
    print("r2 Score : ",r2)
    
    input_data = pd.DataFrame({'TV': [tv_budget], 'radio': [radio_budget], 'newspaper': [newspaper_budget]})
    predicted_sales = model.predict(input_data)
    print("Predicted sales:", predicted_sales[0])

def main():
    print("Machine learning Application")
    print("Advertising Sales Prediction using Linear Regression")

    tv_budget = float(input("Enter TV budget: "))
    radio_budget = float(input("Enter radio budget: "))
    newspaper_budget = float(input("Enter newspaper budget: "))
  
    Advertise(tv_budget, radio_budget, newspaper_budget)

if __name__ == "__main__":
    main()
