tikets = int(input('Введите нужное количество билетов'))
age = int(input('Введите возраст'))
Itogo = 0
for i in range(tikets):
    if 18<= age < 25:
        Itogo = Itogo + 990
    elif age >=25:
        Itogo = Itogo + 1390
    else:
        Itogo = Itogo + 0
print("Сумма к оплате", int(Itogo))
if tikets >=3:
    Itogo = Itogo * 0.9
print("Сумма со скидкой", int(Itogo))


