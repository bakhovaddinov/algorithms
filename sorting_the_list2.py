massive = []
N = int(input('Введите количество элементов массива '))


for i in range(N):
        massive.append(int(input('Введите элементы массива последовательно ')))

i = 0
j = 0
while j < N**2:
        i = 0
        while i < len(massive) - 1:
                if massive[i] > massive [i+1]:
                        massive[i], massive[i+1] = massive[i+1], massive[i]
                i = i + 1
                j = j + 1



print(massive)
