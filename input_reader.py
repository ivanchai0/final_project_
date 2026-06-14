from calculator import evaluate_postfix

class InputReader:
    """Класс для получения выражений от пользователя (вручную или из файла)."""

    def __init__(self, validator):
        self._validator = validator

    def from_keyboard(self):
        print("Введите постфиксное выражение.")
        print("Числа и операторы разделяйте пробелами, например: 5 2 3 / 3 / 5 * +")
        expression = input("> ").strip()
        if not expression:
            print("Ошибка: вы ничего не ввели.")
            return
        self._process(expression)

    def from_file(self):
        filename = input("Введите имя файла (например, expression.txt):\n> ").strip()
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                expression = f.readline().strip()
            if not expression:
                print("Ошибка: файл пуст или первая строка отсутствует.")
                return
            print(f"Из файла прочитано выражение: {expression}")
            self._process(expression)
        except FileNotFoundError:
            print(f"Ошибка: файл '{filename}' не найден. Проверьте имя и попробуйте снова.")
        except IOError as e:
            print(f"Ошибка при чтении файла: {e}")

    def _process(self, expression):
        try:
            self._validator.validate(expression)
            result = evaluate_postfix(expression)
            print(f"Результат: {result}")
        except ValueError as e:
            print(f"Ошибка в выражении: {e}")
        except ZeroDivisionError as e:
            print(f"Математическая ошибка: {e}")
        except RuntimeError as e:
            print(f"Внутренняя ошибка: {e}")