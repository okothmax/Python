num1= int(input('Enter the range of values: '))
num2= int(input('Enter the range of values: '))

print("the prime numbers in the range are:")
my_prime =[]
for number in range(num1,num2+1):
    if number > 1:
        for i in range(2,number):
            if number % 2 ==0:
                break
            else:
                my_prime.append(number)
distinct_prime = set(my_prime)
Q =list(distinct_prime)
print(Q)

big = Q[0]
for m in Q:
    if m > big:
        big = m

'''calculating the factors'''
length = len(Q)
print(f'the length is {length}')
for i in Q:
    k = 1
    while k < big or k == big :
        if i % k == 0:
            print(f'the factors for {i} are {k}')
        k +=1

