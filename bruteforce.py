
import csv

def force_brute(max_value, actions, selected_actions = []):

    if actions:
        val1, profit1, lstval1 = force_brute(max_value, actions[1:], selected_actions)
        val = actions[0]
        if val[1] <= max_value :
            val2, profit2, lstval2 = force_brute(max_value - val[1], actions[1:], selected_actions + [val])
            if profit1 <= profit2:
                return val2, profit2, lstval2

        return val1, profit1, lstval1
    else:
        return sum([i[1] for i in selected_actions]), sum([i[2] for i in selected_actions]), selected_actions



f= open (r"dataset3.csv") 
myReader = csv.reader(f) 
ele = []

for row in myReader:
    ele.append(row)  

ele = ele[1:]
actions = []
max_value = 500

for i in range (0 , len(ele)-1):
   action = ele[i]
   #converting the prices and interest from str to float and int
   action[1] = int(action[1])
   action[2] = float(action[2])
   actions.append(action)

value_invested, profit, selected_shares = force_brute(max_value,actions)

print("Actions bought: ")
print(selected_shares) 
print(" ")
print("Total cost: " + str(value_invested))
print("Total return: " + str(profit))
