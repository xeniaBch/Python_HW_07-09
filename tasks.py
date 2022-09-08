#first level
#first task
print("Task 1")
n = int(input("Enter n "))
for i in range(1,n+1):
    for j in range(0,i):
        print(i," ",end=''*j)
    print()

#second task
print("===================")
print("Task 2")
for a in range (3,21):
    for b in range (3,21):
        for c in range (3,21):
            if (pow(a,2) + pow(b,2) == pow(c,2)):
                print("a=",a, " b=", b, " c=", c)

#second level
print("===================")
print("Level 2")
n = int(input("Enter odd number "))
if(n&2 == 0):
    print("Number is wrong")
else:
    middle = n // 2 + 1
    count = 0
    for i in range(1, n + 1):
        if i > middle:
            count -= 1
        else:
            count += 1
        for i in range(count):
            print('*', end='')
        print()