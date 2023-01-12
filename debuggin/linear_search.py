def linear_search(list,key):
    for i,item in enumerate(list):
        if item == key:
            return i
    return -1

print(linear_search([1,7,9,11],9)) # return should be 2
print(linear_search([9,111,-187,11111],11111)) #result shoud be 3
