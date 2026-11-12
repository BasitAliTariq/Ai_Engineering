# need of list
item1='bread'
item2='fruit'
item3='vegetable'

# Now problem here is if we have hundred of items we need to crete multiple variable 

# List solve this problem

items=['bread','vegetable','fruit']

# printing who;le list
print(items) # ['bread', 'vegetable', 'fruit']

# accessing individual item
print(items[0]) # bread
print(items[2]) # fruit


# modifyng list

items[0]="eggs"
print(items) # ['eggs', 'vegetable', 'fruit']

# accessing range of item
print(items[0:2]) #  ['eggs', 'vegetable']


# neagative indexing]
print(items[-1]) # fruit

# built in methods

print(items) # ['eggs', 'vegetable', 'fruit']
items.append("butter")
print(items) # ['eggs', 'vegetable', 'fruit', 'butter']


print(items) # ['eggs', 'vegetable', 'fruit', 'butter']
items.insert(1,"bread")
print(items) #  ['eggs', 'bread', 'vegetable', 'fruit', 'butter']


# joining two lists
food=['eggs', 'vegetable', 'fruit', 'butter']
bathroom=['shampoo','soap']
print(food+bathroom) #['eggs', 'vegetable', 'fruit', 'butter', 'shampoo', 'soap']

# in operator 
print("eggs" in food) #true
print('carrot' in food) #false

