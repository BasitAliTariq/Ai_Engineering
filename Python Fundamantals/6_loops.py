# 6_loops.py

# Problem :Write a program that store monthly expenses in a list and find out the total expenses for all month

expense=[1200,1000,1200,1300,1400,1500,1600,1700,1800,1900,2000,2100]

sum=0
for i in expense:
  sum=sum+i;
print("The sum of all monte expenses are",sum)



# Problem :Write a program that print number from 1 to  10

for i in range(1,11):
  print(i)
  
  
# Problem :Write a program that store monthly expenses in a list,display expense of each month and find out the total expenses for all month

expense=[1200,1000,1200,1300,1400,1500,1600,1700,1800,1900,2000,2100]

sum=0
for i in range(len(expense)):
  print("Month:",i+1,"Expense:",expense[i])
  sum=sum+expense[i];
print("The sum of all monte expenses are",sum)







# break
# Find the keys of car in location of house
key='chair'
locations=['table','sofa','bed','chair','kitchen','room']
for i in locations:
  if i==key:
    print("your key is found in ",i)
    break
  else:
    print("your key is not found in ",i)
    


# your key is not found in  table
# your key is not found in  sofa
# your key is not found in  bed
# your key is found in  chair


# continue
# write numbers from 1 to 10 except even

for i in range(1,11):
  if i % 2 == 0:
    continue;
  else:
    print(i)

# while loop
# write numbers from 1 to 10 using while loop

i=1
while i<10:
  print(i)
  i=i+1
  
  
  