per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposit = []
money = int(input('Введите сумму вклада'))
for key in per_cent.keys():
    deposit.append (money * per_cent[key]/100)
print(deposit)
max_deposit = max(deposit)
print('Максимальная сумма, которую вы можете заработать —', end= '')
print(max_deposit)