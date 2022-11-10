def Average(Last_Term):
    
    sum = 0
    
    for i in range (1, Last_Term + 1):
        sum += i
    
    return sum / Last_Term

N = int(input("Enter an Integer: "))
print("The Sum ")