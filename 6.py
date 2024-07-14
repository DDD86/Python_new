list_with_duplicates = [1, 1, 2, 3, 4, 4, 4]
list_of_duplicates = set()

# Создаем множество для хранения элементов, которые повторяются
seen = set()
# Множество для хранения элементов, которые встречаются более одного раза
duplicates = set()

for element in list_with_duplicates:
    if element in seen:
        duplicates.add(element)
    else:
        seen.add(element)

print(list(duplicates))
