from stack import Stack

def evaluate_postfix(expression):
    stack = Stack()
    elements = expression.strip().split()
    for elem in elements:
        try:
            number = float(elem)
            if number <= 0:
                raise ValueError(f"Число должно быть положительным, а получено: {elem}")
            stack.push(number)
        except ValueError:
            if elem not in ('+', '-', '*', '/'):
                raise ValueError(f"Недопустимый символ: '{elem}'. Ожидалось число или оператор.")
            try:
                right = stack.pop()
                left = stack.pop()
            except IndexError:
                raise ValueError(
                    "Ошибка в порядке выражения: не хватает чисел для операции. "
                    "Проверьте, что оператор стоит после двух чисел."
                )

            if elem == '+':
                result = left + right
            elif elem == '-':
                result = left - right
            elif elem == '*':
                result = left * right
            else:
                if right == 0:
                    raise ZeroDivisionError("Деление на ноль невозможно.")
                result = left / right

            stack.push(result)

    if stack.size() != 1:
        raise RuntimeError(
            "Внутренняя ошибка: после вычислений осталось больше одного значения. "
            "Скорее всего, выражение составлено неверно."
        )

    return stack.pop()