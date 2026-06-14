class PostfixValidator:
    """Класс для проверки синтаксиса постфиксного выражения."""

    def _is_number(self, token):
        try:
            return float(token) > 0
        except ValueError:
            return False

    def _is_operator(self, token):
        return token in ('+', '-', '*', '/')

    def validate(self, expression):
        if not expression or not expression.strip():
            raise ValueError("Выражение не может быть пустым.")

        elements = expression.strip().split()
        if not elements:
            raise ValueError("Выражение не содержит ни одного элемента.")

        for elem in elements:
            if not (self._is_number(elem) or self._is_operator(elem)):
                raise ValueError(
                    f"Недопустимый элемент: '{elem}'. "
                    "Используйте только положительные числа и знаки операций +, -, *, /."
                )

        # Алгоритм проверки баланса чисел и операторов без вычислений.
        # Каждое число — это значение, оператор берёт два значения и даёт одно.
        # В конце должно остаться ровно одно значение.
        values_count = 0
        for elem in elements:
            if self._is_number(elem):
                values_count += 1
            else:  # оператор
                if values_count < 2:
                    raise ValueError(
                        "Недостаточно чисел для выполнения операции. "
                        "Возможно, оператор стоит раньше, чем нужно. "
                        "Убедитесь, что выражение записано в постфиксной форме."
                    )
                values_count -= 1

        if values_count != 1:
            raise ValueError(
                "Некорректное выражение. "
                "После вычисления должно остаться ровно одно число. "
                "Возможно, лишние числа или не хватает операторов."
            )

        return True