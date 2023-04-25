n = int(input("Ввести число"))
d = 0
while d < n:
    d=d+1
    print('*' * d)


n = int(input("Ввести число"))
q = 0
while q < n:
    q=q+1
    print(' '*(n-q),'*'*q)


n = int(input("Ввести число"))
i = 0
while i in range(n):
    print('*' * n)
    n -= 1

k = int(input("Ввести число"))
q = k
while q > 0:
     print(' '* (k-q), '*' * q)
     q -= 1