print("=== Задача 0 ===")
numbers = []

while True:
    line = input("Введите числа (например: 1 2 10 -1): ").strip()
    if not line:
        continue

    try:
        input_numbers = [int(x) for x in line.split()]
    except ValueError:
        print("Ошибка: вводите только целые числа, разделённые пробелами.")
        continue

    if 0 in input_numbers:
        break

    filtered = [x for x in input_numbers if x > 0 and x % 2 == 0]
    numbers.extend(filtered)

print("Собранные числа:", numbers)
print("Количество чисел:", len(numbers))


print("\n=== Задача 1 ===")
celsius = [0, 15, 25, 30, 40, 100]
fahrenheit = [c * 9/5 + 32 for c in celsius]
print("Температуры в Фаренгейтах:", fahrenheit)

grades = [45, 85, 92, 33, 67, 78, 90, 55, 29, 88]
passed = [g for g in grades if g >= 60]
print("Прошедшие оценки:", passed)

print("\n=== Задача 2 ===")
transactions = [100, -50, 200, -30, 150, -20, 300]
taxes = [t * 0.15 for t in transactions if t > 0]
print("Налоги (15% с доходов):", taxes)

print("\n=== Задача 3 ===")
products = ['футболка', 'кружка', 'блокнот']
colors = ['красный', 'синий', 'зеленый']
combinations = [f"{p} - {c}" for p in products for c in colors]
print("Все комбинации товар–цвет:")
for combo in combinations:
    print("  ", combo)

print("\n=== Задача 4 ===")
employees = [('Иван', 45), ('Мария', 92), ('Петр', 33), ('Анна', 67)]
performance = [
    "Отлично" if score >= 90 else
    "Хорошо" if score >= 60 else
    "Требует улучшения"
    for name, score in employees
]
print("Оценки производительности:", performance)

print("\n=== Задача 5 ===")
sales = [
    {'name': 'Алексей', 'sales': 150, 'returns': 10},
    {'name': 'Ольга', 'sales': 200, 'returns': 5},
    {'name': 'Дмитрий', 'sales': 80, 'returns': 25},
    {'name': 'Елена', 'sales': 300, 'returns': 8}
]

top_managers = [
    s['name'] for s in sales
    if (s['sales'] - s['returns'] >= 150) and (s['returns'] / s['sales'] * 100 < 10)
]

print("Топ-менеджеры:", top_managers)