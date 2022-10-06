#With While
N = float(input("Enter a Interger Greater Than 1:"))
i = 1
a = 0

while N > 1:

    a = (N(N+1)) % 2

print(a)

N = int(input("Enter a Interger Greater Than 1: "))
sum = 0 

# With For 
for i in range(1, N + 1):

    sum += i

Average_Integer = sum / N 

print ("The average of 1, ....", N , "is: ", Average_Integer)

