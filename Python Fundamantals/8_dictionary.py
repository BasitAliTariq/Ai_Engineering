# Dictionaries allow you to store key value pair

# Online Python compiler (interpreter)
# Write and run Python online using this editor.

d={"basit" : 319, "Fahad" : 303, "msd" : 331}

# printing dictionary
print(d) # {'basit': 319, 'Fahad': 303, 'msd': 331}

# accessing elemet in dictionay
print(d["basit"]) # 319

# add an entry in dictionary
d["t"]=321
print(d) # {'basit': 319, 'Fahad': 303, 'msd': 331, 't': 321}

# delete and entry

del d["t"]
print(d) # {'basit': 319, 'Fahad': 303, 'msd': 331}

# print all the dictionary key and  value

for key in d:
  print("key:",key,": value",d[key])





  





