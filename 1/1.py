# от 1 до n включительно

num = int(input("Enter a number: "))
summ = 0
c = 0

if num < 2:
    print ("Число меньше 2")

else:
    for i in range(2, num):
        for j in range(1, num):
            if i % j == 0:
                c +=1

        if c == 2:
            summ += i

        c = 0

print (summ)