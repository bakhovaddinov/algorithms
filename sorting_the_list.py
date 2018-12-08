massive = []
N = int(input('Введите количество элементов массива '))
for i in range(N):
        massive.append(int(input('Введите элементы массива последовательно ')))

for i in range(len(massive)):
        k = i + 1
        for k in range(len(massive)):
                if massive[i] < massive[k]:
                        massive[i], massive[k] = massive[k], massive[i]



print(massive)
