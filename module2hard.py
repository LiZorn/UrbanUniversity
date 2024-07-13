def matrix(x):
    result = []
    for i in range(1, x):
        for n in range(i + 1, x):
            plus = i + n
            if x % plus == 0:
                result.append(i)
                result.append(n)
            else:
                continue
    print(result)
    return matrix


n = int(input(f'Введите число от 3 до 20 включительно: '))
matrix(n)
