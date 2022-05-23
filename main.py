thaco=input('ThAC0:')
thaco=int(thaco)
ac=input('AC:')
ac=int(ac)
dice=input('Dice:')
dice=int(dice)
x= thaco-ac

if dice > 19:
  print('CRITICAL')
elif x <= dice:
  print('Attack Hit')
else:
  print('Miss')