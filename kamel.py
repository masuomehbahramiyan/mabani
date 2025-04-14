n = int(input('Enter n:'))
x=0
for i in range(1,n):
    if n%i==0:
        x= x+i
if x==n:
    print('YES')
else:
    print ('NO')