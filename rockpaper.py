import random
my_list =[]
for k in range(2,7):
    my_list.append(k)

prime_numbers =[]
for k in my_list:
    if k > 1 :
        for i in range(2,int(k/2)+1):
            if (k % i) == 0:
                break
        else:
            prime_numbers.append(k)

p = random.choice(prime_numbers)
print("P is {}".format(p))
q = random.choice(prime_numbers)
print("Q is {}".format(q))
N = p * q
encryption = []
encryption.append(N)
print("The encryption is, ", encryption)
print("N is {}".format(N))
phi_calc =[]
for k in range(N+1):
    if k > 0:
        phi_calc.append(k)
print(phi_calc)

co_prime = (p-1)*(q-1)
print("Co-prime is {}".format(co_prime))