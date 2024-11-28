import random


# Функция для чтения файла с переводами
def load_words(file_path):
    words = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            if '-' in line:
                parts = line.strip().split(' - ')
                english = parts[0].split(', ')
                russian = parts[1].split(', ')
                words.append((english, russian))
    return words


# Функция для записи статистики
def save_stats(total, correct, file_path="stats.txt"):
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(f"Заданий было {total}, решено верно {correct}\n")


# Логика тренировки
def train(words, mode):
    total_questions = 0
    correct_answers = 0

    try:
        while True:
            total_questions += 1
            if mode == 1:  # Английское слово, варианты русского
                random_entry = random.choice(words)
                word = random.choice(random_entry[0])
                correct_answer = random.choice(random_entry[1])
                options = random.sample([w for _, trans in words for w in trans], 3) + [correct_answer]
                random.shuffle(options)
                print(f"Переведите: {word}")
            else:  # Русское слово, варианты английского
                random_entry = random.choice(words)
                word = random.choice(random_entry[1])
                correct_answer = random.choice(random_entry[0])
                options = random.sample([w for trans, _ in words for w in trans], 3) + [correct_answer]
                random.shuffle(options)
                print(f"Переведите: {word}")

            # Вывод вариантов
            for i, option in enumerate(options, 1):
                print(f"{i}. {option}")

            # Пользовательский ввод
            try:
                user_choice = int(input("Ваш ответ (номер): "))
                if options[user_choice - 1] == correct_answer:
                    print("Ты молодец!")
                    correct_answers += 1
                else:
                    print(f"Неверно. Правильный ответ: {correct_answer}")
            except (ValueError, IndexError):
                print("Некорректный ввод!")

            # Предложить завершить
            cont = input("Хотите продолжить? (да/нет): ").strip().lower()
            if cont != "да":
                break
    finally:
        save_stats(total_questions, correct_answers)


# Основная функция
def main():
    words_file = input("Введите путь к файлу со словами (например, words.md): ").strip()
    words = load_words(words_file)

    print("\nВыберите режим:")
    print("1. Перевод английского на русский")
    print("2. Перевод русского на английский")

    try:
        mode = int(input("Ваш выбор (1 или 2): ").strip())
        if mode not in [1, 2]:
            raise ValueError("Выберите 1 или 2")
    except ValueError:
        print("Некорректный ввод! Завершение программы.")
        return

    train(words, mode)


if __name__ == "__main__":
    main()
