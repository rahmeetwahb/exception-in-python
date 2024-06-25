import sys

print('program pertambahan bilangan')

a = float(input('Input a: '))
b = float(input('Input b: '))

try:
    hasil = a + b
except:
    print('ERROR: Nilai b tidak boleh nol')
    sys.exit()

#show data
print('\na: ', a)
print('b: ', b)
print('a + b: ', a + b)