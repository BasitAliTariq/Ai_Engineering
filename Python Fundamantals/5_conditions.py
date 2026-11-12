# Problem :Write a program that ask user to enter numer .Program should then tell the is even or odd

num=int(input("Enter the number:"))
if num%2==0:
  print("Your number",num,"is even")
else:
   print("Your number",num,"is odd")
   


# Problem :Write a program that asks users to enter dish name and it should print which cousine is that dish

pakistani_cousine=['samosa','daal','chanay','naan']
italian_cousine=['pizza','pasta','rizoto']
chinese_cousine=['egg role','pot sticker','fried rice']

dish=input("Enter the name of dish")

if dish in pakistani_cousine:
  print("pakistani")
elif dish in italian_cousine:
  print("Italian")
elif dish in chinese_cousine:
  print("Chinese")
else:
  print("Your dish is not our knowlege base")
  