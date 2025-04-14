a=int(input('Enter a:'))
b=int(input('Enter b:'))
c = a-b
if b>a:
    print('Wrong orger!')
elif (a-b)%2!=0:
    print('Worng difference!')
else:
    for i in range (a):
        if i <(c//2) or i>=(c//2)+b:
            print('* '*a)
        else:
            print('* '*(c//2),'  '*b,'* '*(c//2),sep='')