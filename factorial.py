n = int(input('Enter n:'))
f = 1
if n > 0 :
    for i in range(1, n+1):
        f = f * i
print('factorial:', f)