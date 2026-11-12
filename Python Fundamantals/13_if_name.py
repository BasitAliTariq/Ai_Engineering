def calculate_sum(expense,person):
  total=0
  for i in expense:
    total=total+i
  print('The total',person,"epense is",total)


if __name__ == "__main__":
  basit_expense=[1000,2000,3000,4000]
  fahad_expense=[3000,4000,6000,2000]

  calculate_sum(basit_expense,'Basit')
  calculate_sum(fahad_expense,'Fahad')