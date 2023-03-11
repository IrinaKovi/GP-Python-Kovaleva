profit = float(input("Введите выручку фирмы "))
costs = float(input("Введите издержки фирмы "))
if profit > costs:
    print(f"Фирма работает с прибылью")
elif profit == costs:
    print("Фирма работает в ноль")
else:
    print("Фирма работает в убыток")