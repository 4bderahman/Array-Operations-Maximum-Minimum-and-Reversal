def Max(T):
    Max = T[0]
    for i in range(10):
        if Max < T[i] :
            Max = T[i]
    return Max

def Min(T):
    Min = T[0] 
    for i in T :
        if Min > i :
            Min = i
    return Min        

def reverse(T):
    New = [] 
    for i in range(9 , -1 , -1):
        New.append(T[i])
    return New

T = [0.0] * 10

for i in range(10):
    T[i] = float(input(f"Donner l'élément {i + 1} :"))

print("Le Maximum est :", Max(T))
print("Le Minimum est :", Min(T))
print("Le tableau reverser est :", reverse(T))