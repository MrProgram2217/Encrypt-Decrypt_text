import time

russian = ['о', 'а', 'е', 'и', 'т', 'н', 'р', 'ж', 'з', 'г', 'й', 'к', 'л', 'м', 'в', 'б', 'п', 'ё', 'с', 'д', 'у',
          'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'я', 'ы', 'ь', 'э', 'ю', 'ъ', ' ', '\n', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ',', '.', '!', '?']
crypt   = ['Ё', '#', '4', '/', '}', '2', '№', 'y', '|', '*', '(', '@', 'h', '&', '=', '+', '%', '-', '_', 'Д', '1',
          ':', ']', '{', '~', 'т', '<', '$', ';', 'Ж', 'Џ', '0', '6', 'v', '\n', 'Ђ', 'Ў', '"', '>', 'µ', 'Є', 'ћ', '^', 'Ї', 'Ѕ', 'Э', '`', 'Ъ', 'Ц']

print('Decrypt program')
decrypted_text = ''
e = str(input('введите название файла:  '))
fileName = e + '.txt'

keyfile = str(input('введите название файла ключа:  '))
keyfileName = keyfile + '.txt'

start_time = time.time()

print('decryption start...')
f = open(fileName, 'r')
lenText = len(f.read()) + 1
f.seek(0)

f3 = open(keyfileName, 'r')

print('название файла: ',fileName)
print('название файла ключа: ',keyfileName)

for i in range (1, lenText):
    enc = f.read(1)
    key = int(f3.read(1))
    try:
        encIndex = crypt.index(enc) - key
        print(encIndex)
        rus = russian[encIndex]
    except:
        rus = enc
        print('ошибочка с элементом ', enc, ' ', key)
    decrypted_text += rus

print(decrypted_text)
f2 = open('decrypted_gen.txt', 'w')
f2.write(decrypted_text)

print('successfully decrypded')
print("--- %s seconds ---" % (time.time() - start_time))
input('tap for exit')
