new_list = [1, 2, 3, 4]
result = new_list[0]
print(result) # print the element at index 0

#searching in arrayys
if 1 in new_list:
    print(True)

for n in new_list:
    if n == 1:
        print(True)
        break

print(len(new_list)) 
new_list.extend([8,9])
print(new_list)
print(new_list.pop())