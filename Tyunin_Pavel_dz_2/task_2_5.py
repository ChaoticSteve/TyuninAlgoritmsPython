'''
Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.
'''

chr_gen = ((num, chr(num)) for num in range(32, 128))
try:
    while chr_gen:
        for _ in range(10):
            alikey, alivalue = next(chr_gen)
            print(f'{alikey}: {alivalue}', end='\t')
        print()
except StopIteration:
    print('')