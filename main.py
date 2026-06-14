from validators import PostfixValidator
from input_reader import InputReader


def print_menu():
    print("\n" + "=" * 50)
    print("  КАЛЬКУЛЯТОР ПОСТФИКСНЫХ ВЫРАЖЕНИЙ")
    print("=" * 50)
    print("1. Ввести выражение вручную")
    print("2. Загрузить выражение из файла")
    print("3. Выход")
    print("-" * 50)


def main():
    print("Добро пожаловать в калькулятор постфиксной записи!")
    print("Поддерживаются операции: +, -, *, /")
    print("Числа должны быть положительными, разделитель — пробел.")
    print("Пример правильной записи: 5 2 3 / 3 / 5 * +")
    print("Это соответствует обычному выражению: 5 + ((2 / 3) / 3) * 5\n")

    validator = PostfixValidator()
    reader = InputReader(validator)

    while True:
        print_menu()
        choice = input("Выберите действие (1-3): ").strip()

        if choice == '1':
            reader.from_keyboard()
        elif choice == '2':
            reader.from_file()
        elif choice == '3':
            print("До свидания!")
            break
        else:
            print("Неверный ввод. Пожалуйста, введите 1, 2 или 3.")


if __name__ == "__main__":
    main()
