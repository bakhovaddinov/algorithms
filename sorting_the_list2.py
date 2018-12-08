massive = []
N = int(input('Введите количество элементов массива '))


for i in range(N):
        massive.append(int(input('Введите элементы массива последовательно ')))

for i in range(len(massive) - 1):
        if massive[i] > massive [i+1]:
                massive[i], massive[i+1] = massive[i+1], massive[i]



print(massive)
