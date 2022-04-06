'''
Определение количества различных подстрок с использованием хэш-функции.
Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
Требуется найти количество различных подстрок в этой строке.
'''

import hashlib


def substring_counter(some_string):
    hash_set = set()
    for i in range(len(some_string) + 1):
        for j in range(len(some_string) - 1 if i == 0 else len(some_string), i, -1 ):
            h = hashlib.sha1(some_string[i:j].encode('utf-8')).hexdigest()
            hash_set.add(h)

    return len(hash_set)


print(substring_counter('dsfsidfiasdnfisadnfjasndfiwqemnpoqwie'))
