from sklearn import tree

def WhetherPlayCondition(Whether, Temprature):
    print("Weather classification case study")

    features = [[1, 35], [1, 35], [3, 35], [2, 37], [2, 36], [2, 36], [3, 36], [1, 37], [1, 36], [2, 37], [1, 37], [3, 37], [3, 36], [2, 37], [2, 37]]
    labels = [2, 2, 1, 1, 1, 2, 1, 2, 1, 1, 1, 1, 1, 2, 1]

    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(features, labels)

    prediction = clf.predict([[Whether, Temprature]])

    if prediction == 1:
        print("You play in this condition.")
    elif prediction == 2:
        print("You don't play in this condition.")

def main():
    print("-----Weather type classification study-----")

    print("Enter the weather condition (Sunny, Rainy, Overcast): ")
    Whether = input()

    print("Enter temperature (Hot, Cool, or Mild): ")
    Temp = input()

    if Whether.lower() == "sunny":
        Whether_value = 1
    elif Whether.lower() == "rainy":
        Whether_value = 2
    elif Whether.lower() == "overcast":
        Whether_value = 3
    else:
        print("Invalid weather option")
        return

    if Temp.lower() == "hot":
        Temp_value = 35
    elif Temp.lower() == "cool":
        Temp_value = 36
    elif Temp.lower() == "mild":
        Temp_value = 37
    else:
        print("Invalid temperature option")
        return

    WhetherPlayCondition(Whether_value, Temp_value)

if __name__ == "__main__":
    main()
