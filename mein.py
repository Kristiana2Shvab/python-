n = int (input('Введите трёхзначное число: '))
c = n %10
n = n // 10
b = n %10
a = n // 10
summ = c + b + a
print (summ)
