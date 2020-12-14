num = int(input("Enter number : "))
list = range(1,num+1)
divisors = []
for i in list : 
    if num % i == 0 :
        divisors.append(i)
print("All divisiors of given number are ")
print(divisors)