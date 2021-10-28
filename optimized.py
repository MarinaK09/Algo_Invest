import csv

def optimisation(max_value, actions):

    #The matrix is initialized to 0 
    matrice = [[0 for x in range(max_value + 1)] for x in range(len(actions) + 1)]
    # the calculus goes through all the actions
    for i in range(1, len(actions) + 1) :
        #For each action we go through the max value
        for weigth in range(1, max_value + 1) :
            # If the value of the current action is less than the current max value
            if actions[i-1][1] <= weigth :
                # Comparing the current optimum value to the precedent optimum value
                matrice[i][weigth] = max(actions[i-1][2] + matrice[i-1][weigth-actions[i-1][1]], matrice[i-1][weigth])
            else :
                matrice[i][weigth] = matrice[i-1][weigth]
    

    weigth = max_value
    n = len(actions)
    selected_actions = []

# Selecting all the actions that led to the optimum investment 
    while weigth >= 0 and n >= 0 :
        element = actions[n-1]
        if matrice[n][weigth] == matrice[n-1][weigth-element[1]] + element[2] :
            selected_actions.append(element)
            weigth -= element[1]

        n -= 1
    
    return matrice[-1][-1], selected_actions, sum([i[1] for i in selected_actions])




f= open (r"dataset2.csv") 
myReader = csv.reader(f) 
ele = []

for row in myReader:
    ele.append(row)  

ele = ele[1:]
actions = []
#max_value is multiplied by 100 because the cost of each action is also multiplied by 100 to convert it into an int
max_value = 500*100

for i in range (0 , len(ele)-1):
   action = ele[i]
   #converting the prices and interest from str to float and int
   action[1] = float(action[1])
   action[2] = float(action[2])
   #Calculating the exact profit of each action
   action[2] = (action[2]*action[1])/100
   #Multiplying the price of each action by 100 to convert it into an int
   action[1] = int(action[1]*100)
   #Deleting the actions with a negative or zero price
   if action [1] > 0:
       actions.append(action)


(profit, selected_shares, invested_value) = optimisation(max_value,actions)
print("Actions bought: ")
print(selected_shares) 
print(" ")
print("Total cost: " + str(invested_value/100))
print("Total return: " + str(profit))
