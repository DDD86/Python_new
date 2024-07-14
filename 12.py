names = ['Alice', 'Bob', 'Charlie']
rates = [1000, 1500, 1200]
bonuses = ['10.25%', '8.5%', '12.75%']

result_dict = {name: rate * (1 + float(bonus.strip('%')) / 100) for name, rate, bonus in zip(names, rates, bonuses)}
print(result_dict)
