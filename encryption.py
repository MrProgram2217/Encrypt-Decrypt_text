import time
from random import *

russian = ['о', 'а', 'е', 'и', 'т', 'н', 'р', 'ж', 'з', 'г', 'й', 'к', 'л', 'м', 'в', 'б', 'п', 'ё', 'с', 'д', 'у',
          'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'я', 'ы', 'ь', 'э', 'ю', 'ъ', ' ', '\n', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ',', '.', '!', '?']
crypt   = ['Ё', '#', '4', '/', '}', '2', '№', 'y', '|', '*', '(', '@', 'h', '&', '=', '+', '%', '-', '_', 'Д', '1',
          ':', ']', '{', '~', 'т', '<', '$', ';', 'Ж', 'Џ', '0', '6', 'v', '\n', 'Ђ', 'Ў', '"', '>', 'µ', 'Є', 'ћ', '^', 'Ї', 'Ѕ', 'Э', '`', 'Ъ', 'Ц']

print('Encrypt program v2 \n')
encrypted_text = ''
encrypt_key = ''
e = str(input('введите название файла:  '))
fileName = e + '.txt'

start_time = time.time()

print('encryption start')

f = open(fileName, 'r')           # открытие файла и его длина
lenText = len(f.read()) + 1
f.seek(0)
print('название файла: ',fileName)

for i in range (1, lenText):        # замена элементов    
    rus = f.read(1)
    try:
        rusIndex = russian.index(rus)
        key = randint(0,9)
        if rusIndex + key < lenText:
            rusIndex += key
        else:
            key = 0
        encrypt_key += str(key)
        enc = crypt[rusIndex]
    except: 
        enc = rus
        key = 0
        encrypt_key += str(key)
        print('Такого символа не знаю, поэтому оставляю как есть. ','(индекс знака:', i,') ',rus)
    encrypted_text += enc

f2 = open('crypt.txt', 'w')
f2.write(encrypted_text)

f3 = open('crypt_key.txt', 'w')
f3.write(encrypt_key)

print('successfully encrypted')
print("--- %s seconds ---" % (time.time() - start_time))
input('Enter')