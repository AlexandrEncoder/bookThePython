

n = int(input('Table of : '))

i= int(input('Enter the beginning of the multiplication table:\n'))

f = int(input('Enter the end of the multiplication table:\n')) 


while i <= f:
    print(f'{n}x{i}={n*i}')
    i+=1 