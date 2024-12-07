import random

class Encryptor:
    def __init__(self, *numbers):
        self._numbers = numbers  # Инкапсуляция данных
        self._result = self._process_numbers()  # Результат вычисления

    def _process_numbers(self):
        operation = random.choice(['+', '-', '*', '/'])
        if operation == '+':
            return sum(self._numbers)
        elif operation == '-':
            result = self._numbers[0]
            for num in self._numbers[1:]:
                result -= num
            return result
        elif operation == '*':
            result = 1
            for num in self._numbers:
                result *= num
            return result
        elif operation == '/':
            result = self._numbers[0]
            for num in self._numbers[1:]:
                result /= num if num != 0 else 1  # Защита от деления на ноль
            return result

    def __str__(self):
        return f"Encrypted result: {self._result}"


# Пример использования
encryptor = Encryptor(10, 5, 2)
print(encryptor)
