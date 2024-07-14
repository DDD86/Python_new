def pack_backpack(items, max_weight):
    n = len(items)

    # Создаем двумерный массив для хранения максимальной массы, которую можно унести с учетом текущих вещей
    dp = [[0 for _ in range(max_weight + 1)] for _ in range(n + 1)]

    # Преобразуем словарь в список кортежей (название, масса)
    item_list = list(items.items())

    # Заполняем массив dp
    for i in range(1, n + 1):
        item_name, item_weight = item_list[i - 1]
        for w in range(max_weight + 1):
            if item_weight <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - item_weight] + item_weight)
            else:
                dp[i][w] = dp[i - 1][w]

    # Восстановление списка вещей, которые можно положить в рюкзак
    packed_items = []
    w = max_weight
    for i in range(n, 0, -1):
        item_name, item_weight = item_list[i - 1]
        if dp[i][w] != dp[i - 1][w]:
            packed_items.append(item_name)
            w -= item_weight

    return packed_items

# Пример использования
items = {
    'спальник': 3,
    'еда': 2,
    'вода': 5,
    'палатка': 7,
    'фонарик': 1
}
max_weight = 10

result = pack_backpack(items, max_weight)
print(f"Вещи, которые можно положить в рюкзак с максимальной грузоподъемностью {max_weight}:")
print(result)
