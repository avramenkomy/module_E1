import random

more = "Да"

WORDS = ['skillfactory', 'testing', 'blackbox', 'pytest', 'unittest', 'coverage']
count = 4
step_count = 1
already_letters = []

def secret_word():
    return random.choice(WORDS)

def displayed_secret_string(str):
    print("Загаданное слово: {}".format(''.join(str)))

def guess_letter(count, step_count):
    letter = input("Шаг {}. Кол-во жизней {}.Введите букву: ".format(step_count, count)).strip().lower()
    step_count += 1
    return letter, step_count

def check_len_letter(letter):
    if len(letter) == 1:
        return True
    else:
        return False

def check_letter(letter, word):
    if letter in word:
        return True
    else:
        return False


def string_refactor(letter, word, secret_string):
    for i in range(len(word)):
        if letter == word[i]:
            secret_string[i] = letter
    return secret_string

def count_decrement(count):
    count -= 1
    return count

#Game
def game():

    more = "Да"
    count = 4
    step_count = 1

    while True:

        if more == "Да":

            # Загадывание слова
            word = secret_word()

            # Формирование строки с пропусками
            secret_string = ['_' for letter in word]
            # Показываем игроку секретную строку
            displayed_secret_string(secret_string)

            # Отгадываем буквы
            while True:
                if count:
                    letter, step_count = guess_letter(count, step_count)

                    # Проверяем корректность ввода
                    if not check_len_letter(letter):
                        print("Неверный ввод. Вводите только одну букву из латинского алфавита.")
                        continue
                    elif letter in already_letters:
                        print("Вы уже называли эту букву")
                        continue

                    # Добавляем букву в список использованных
                    already_letters.append(letter)

                    # Проверяем есть ли буква в слове
                    if check_letter(letter, word):
                        print("Такая буква есть в слове")

                        # Заменяем пропуск на букву
                        string_refactor(letter, word, secret_string)
                        # for i in range(len(word)):
                        #     if letter == word[i]:
                        #         secret_string[i] = letter

                        # Выводим секретную строку
                        displayed_secret_string(secret_string)

                        # проверка слова целиком
                        if input("Вы готовы назвать слово целиком? Да/Нет: ").strip().lower() == "да":
                            if input("Введите слово: ").strip().lower() == word:
                                result = "Вы выиграли"
                                break
                            else:
                                print("Неверное слово")
                                # декремент счетчика
                                count = count_decrement(count)

                        # Если все отгадано по буквам
                        if "_" not in secret_string:
                            result = "Вы выиграли"
                            break

                    else: # если такой буквы нет
                        # декремент счетчика
                        count = count_decrement(count)
                        print("Такой буквы нет! Кол-во жизней: {}".format(count))
                        # Выводим секретную строку
                        displayed_secret_string(secret_string)
                        continue
                else:
                    result = "Вы проиграли"
                    break
        else:
            break

        count = 4
        step_count = 1
        already_letters.clear()
        print(result)
        more = input("Сыграть еще раз? Да/Нет: ").strip()

if __name__ == "__main__":
    game()