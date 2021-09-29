
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

ele = [('action_1',20.2,20*1.05),
       ('action_2',30,30*1.1),
       ('action_3',50,50*1.15),
       ('action_4',70,70*1.20),
       ('action_5',60,60*1.17),
       ('action_6',80.1,80*1.25),
       ('action_7',22,22*1.07),
       ('action_8',26,26*1.11),
       ('action_9',48,48*1.13), 
       ('action_10',34,34*1.27),
       ('action_11',42,42*1.17),
       ('action_12',110,110*1.09),
       ('action_13',38,38*1.23),
       ('action_14',14,14*1.01), 
       ('action_15',18,18*1.03), 
       ('action_16',8,8*1.08),
       ('action_17',4,4*1.12),
       ('action_18',10,10*1.14),
       ('action_19',24,24*1.21),
       ('action_20',114,114*1.18)]

#f = open(dataset1.csv, 'w', encoding="utf-8")

#print(force_brute(500,ele))

print(optimisation(500,ele))
