import pulp

model = pulp.LpProblem("Maximize_Production", pulp.LpMaximize)

lemonade = pulp.LpVariable('Lemonade', lowBound=0, cat='Integer')
fruit_juice = pulp.LpVariable('Fruit_Juice', lowBound=0, cat='Integer')

model += 2 * lemonade + 1 * fruit_juice <= 100, "Water_Limit"
model += 1 * lemonade <= 50, "Sugar_Limit"
model += 1 * lemonade <= 30, "Lemon_Juice_Limit"
model += 2 * fruit_juice <= 40, "Fruit_Puree_Limit"

model += lemonade + fruit_juice

model.solve()

lemonade_amount = pulp.value(lemonade)
fruit_juice_amount = pulp.value(fruit_juice)
total_amount = lemonade_amount + fruit_juice_amount

print(f"Кількість Лимонаду: {lemonade_amount}")
print(f"Кількість Фруктового соку: {fruit_juice_amount}")
print(f"Загальна кількість: {total_amount}")