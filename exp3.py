
# Q1

n = int(input("number to print:"))
i=0
for i in range(1, n+1):
   print(i)



#Q2

n = int(input("to print even numbers upto:"))  
i=0
for i in range(1, n+1):
   if i%2==0:
       print(i)




#Q3

n= int (input("to print odd numbers upto:"))
i=0
for i in range(1, n+1):4

      print(i)


#Q4

n= int(input("enter the value of n:"))

i=1
while i<=n*n:
    print(i, end =" ")
    i=i*2



# Q5

n= int(input("enter the value of n:"))

fact = 1
sum = 1
for i in range(1, n + 1):
    fact =fact*1
    sum = sum + (1/fact)

    print(sum)




# Q6

x = float(input("Enter the value of x: "))

sum = 1
fact = 1
sign = -1

for i in range(2, n + 1, 2):
    fact = 1
    for j in range(1, i + 1):
        fact = fact * j

    term = (x ** i) / fact
    sum = sum + sign * term
    sign = sign * -1

print("cos(", x, ") =", sum)






# Q.7]

import math

n = int(input("Enter a number: "))

root = int(math.sqrt(n))

if root * root != n:
    print("Square root is not a whole number.")
else:
    prime = True

    if root < 2:
        prime = False
    else:
        for i in range(2, root):
            if root % i == 0:
                prime = False
                break

    if prime:
        print(root, "is prime.")
    else:
        print(root, "is not prime.")





# Q8

for i in range(3):
    for j in range(3):
        print(chr(65 + i) + chr(65 + j), end=" ")
        print()




# Q9

n = int(input("Enter the value of n: "))

for i in range(1, n + 1):
    for j in range(i):
        print(chr(65 + j), end=" ")
         print()


#  Q10

n = int(input("Enter the value of n: "))

for i in range(n, 0, -1):
    for j in range(i):
        print(chr(65 + j), end=" ")
    print()



# Q11

n = int(input("Enter the value of n: "))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()



# Q12

n = int(input("Enter the value of n: "))

for i in range(1, n + 1):
    for j in range(i):
        print(i, end=" ")
    print()

