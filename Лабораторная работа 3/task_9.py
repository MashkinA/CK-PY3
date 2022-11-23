salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен
credit_ = 0
money_capital = 0  # количество денег, чтобы прожить 10 месяцев

for _ in range(months):
    credit_ = spend - salary
    spend *= 1 + increase
    money_capital += credit_

print(round(money_capital))
