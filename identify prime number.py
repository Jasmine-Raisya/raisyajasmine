#Raisya Jasmine Zahira
#method 1 
num = int(input("Enter a number"))
if num > 1:
    for i in range(2,int(num/2+1)):
        #starts from 2 and tries all integers (i) between 2 and num/2+1 (the maximum denominator)
        if (num%i) == 0:
            #checks if integer has a remainder with i
            print(num, "is not a prime number")
            break
        else:

            print(num, "is a prime number")

    else:
        print(num, "is not a prime number")

