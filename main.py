#Преобразуйте строку в нижний регистр, чтобы игнорировать различия в регистре символов.
#Удалите из строки все пробелы, знаки препинания и специальные символы, оставив только буквы и цифры.
#Определите длину очищенной строки.
#Используйте цикл для сравнения символов с начала и конца строки:
#- Сравните первый и последний символы.
#- Затем второй и предпоследний.
#- Продолжайте, пока не достигнете середины строки.
#Если все пары символов совпадают, строка является палиндромом.
#Если найдена хотя бы одна пара не совпадающих символов, строка не является палиндромом.


import string

def is_palindrome(s):
    s = s.lower()
    s = ''.join(char for char in s if char.isalnum())
    length = len(s)
    for i in range(length // 2):
        if s[i] != s[length - i - 1]:
            return False

    return True

print(is_palindrome("Привет мир!"))
print(is_palindrome("нажал кабан на баклажан"))             