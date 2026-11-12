#  Functions are the code of block that perform specific task



# Problem :You are given two lists of numbers and you need to find the total of each of these list without functions

basit_expense=[1000,2000,3000,4000]
fahad_expense=[3000,4000,6000,2000]

total=0

for i in basit_expense:
  total=total+i;

print("The toatal basit_expense is",total)


total=0

for i in fahad_expense:
  total=total+i;

print("The toatal fahad_expense is",total)


# As you can see that we need to write the same code again and again




# Problem :You are given two lists of numbers and you need to find the total of each of these list using functions

def calculate_sum(expense,person):
  total=0
  for i in expense:
    total=total+i
  print('The total',person,"epense is",total)


basit_expense=[1000,2000,3000,4000]
fahad_expense=[3000,4000,6000,2000]

calculate_sum(basit_expense,'Basit')
calculate_sum(fahad_expense,'Fahad')

