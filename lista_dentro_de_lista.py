
a = ["apple", "banana", "cherry"]
b = ["Ford", "BMW", "Volvo"]

a.append(b)

'''
#print(a)


count = 0
for item_a in a:
    if count == 3:
        for item_b in item_a:
             print(item_b)

    if count < 3:
        print(item_a)
    count += 1

'''

for item in a:
    if isinstance(item, list):
        for sub_item in item:
            print(sub_item)
    
    else:
        print(item)

