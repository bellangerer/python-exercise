# Übung mit Rene: 26.04

while True:
  to_pay = int(input('To pay:'))
  if to_pay <= 0:
    print('Negative input is invalid')
    continue

  amount_received = int(input('Amount received'))
  if amount_received <= 0:
   print('Negative input is invalid')
   continue

  if amount_received < to_pay:
    print('Amount received mus be greater than amount to pay')
    continue
  print(f'Amount received is {amount_received-to_pay}')
