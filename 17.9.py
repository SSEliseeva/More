array = list(map(int, input("введите последовательность чисел через пробел").split()))
element = int(input())

array.append(element)
print(array)

for i in range(len(array)):  # проходим по всему массиву
    idx_min = i  # сохраняем индекс предположительно максимального элемента
    for j in range(i, len(array)):
        if array[j] < array[idx_min]:
            idx_min = j
    if i != idx_min:  # если индекс не совпадает с максимальным, меняем
        array[i], array[idx_min] = array[idx_min], array[i]

print(array)

def binary_search(array, element, left, right):
    try:
        if left > right:  # если левая граница превысила правую,
            return False  # значит элемент отсутствует

        middle = (right + left) // 2  # находим середину
        if array[middle] == element:  # если элемент в середине,
            return middle  # возвращаем этот индекс
        elif element < array[middle]:  # если элемент меньше элемента в середине
            # рекурсивно ищем в левой половине
            return binary_search(array, element, left, middle - 1)
        else:  # иначе в правой
            return binary_search(array, element, middle + 1, right)
    except IndexError:
        return "число не входит в диапазон списка"

print((binary_search(array, element, 0, len(array))) - 1)
