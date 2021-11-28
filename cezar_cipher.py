print('Добро пожаловать в мир шифра!')

eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
rus_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
rus_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"


ci_or_no = input('Шифрование или дешифрование(+/-): ')
language = input('Выберите язык(r/e): ')
cipher = input('Введите шифр: ')


def caesar_cipher(mod, lang_up, lang_low):
    key = int(input('Введите ключ шифрования: '))
    if ci_or_no == '-':
        key = -key
    total_cipher = ''  # зашифрованная фраза
    for i in range(len(cipher)):  # цикл длинной с фразу
        if cipher[i].isalpha():  # если буква
            if cipher[i] == cipher[i].lower():  # если буква большая
                for j in range(mod):  # цикл поиска по строке алфавита
                    if cipher[i] == lang_low[j]:  # если буква из шифра равно букве из строки алфавита
                        total_cipher += lang_low[(j+key) % mod]  # добавляем в тотал букву[(номер буквы в троке алфавита + ключ)%количество букв]
            if cipher[i] == cipher[i].upper():
                for j in range(mod):  # цикл поиска по строке алфавита
                    if cipher[i] == lang_up[j]:  # если буква из шифра равно букве из строки алфавита
                        total_cipher += lang_up[(j+key) % mod]  # добавляем в тотал букву[(номер буквы в троке алфавита + ключ)%количество букв]
        else:
            total_cipher += cipher[i]
    return total_cipher


def start_program(): #начало программы
    if language == 'r':
        print(caesar_cipher(32, rus_upper_alphabet, rus_lower_alphabet))
    if language == 'e':
        print(caesar_cipher(26, eng_upper_alphabet, eng_lower_alphabet))
    answer()


def answer():#роверка на правильность ответа, чтобы не вводить заново все данные в случае неправильного шифрования
    answer = input('Расшифровка верна? +/- ')
    if answer == '-':
        start_program()
    if answer == '+':
        print('Не благодари)')

start_program()