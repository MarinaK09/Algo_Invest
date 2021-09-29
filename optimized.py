import csv

def optimisation(max_value, actions):
    matrice = [[0 for x in range(max_value + 1)] for x in range(len(actions) + 1)]

    for i in range(1, len(actions) + 1) :
        for w in range(1, max_value + 1) :
            if actions[i-1][1] <= w :
                matrice[i][w] = max(actions[i-1][2] + matrice[i-1][w-int(round(actions[i-1][1]))], matrice[i-1][w])
            else :
                matrice[i][w] = matrice[i-1][w]
    

    w = max_value
    n = len(actions)
    action_selection = []

    while w >= 0 and n >= 0 :
        e = actions[n-1]
        if matrice[n][int(float(w))] == matrice[n-1][int(round(w-e[1]))] + e[2] :
            action_selection.append(e)
            w -= e[1]

        n -= 1
    
    return matrice[-1][-1], action_selection




f= open (r"dataset1.csv") 
myReader = csv.reader(f) 
ele = []

for row in myReader:
    ele.append(row)  

ele = ele[1:]
actions = []
#action = ele[1]
#action[1] = float(action[1])
#action[2] = float(action[2])
#actions.append(action)
for i in range (0 , len(ele)-1):
   action = ele[i]
   action[1] = float(action[1])
   action[2] = float(action[2])
   actions.append(action)

print(actions[999][2])
#print(optimisation(500,actions))
