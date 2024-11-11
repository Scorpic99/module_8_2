from logging import exception


def personal_sum(numbers):
    incorrect_data = 0
    result = 0
    counter = 0
    for i in numbers:
        try:
            if isinstance(i, int):
                result += i
                counter += 1
            else:
                incorrect_data += 1
                raise TypeError('error in incorrect data')
        except TypeError:
            print(f"Некорректный тип данных для подсчета суммы - {i}")

    return result, incorrect_data, counter


def calculate_average(numbers):
    try:
        if not isinstance(numbers, list) and not isinstance(numbers, str):
            raise TypeError('В numbers записан некорректный тип данных')
    except TypeError as exc:
        print(exc.args[0])
        return None

    m_sum = personal_sum(numbers)

    for i in numbers:
        try:
            if m_sum[0] / m_sum[2]:
                return m_sum[0] / m_sum[2]
        except ZeroDivisionError:
            print('Devision to 0')
            return 0
    return str(m_sum[0] / len(numbers))


try:
    print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка перебирается, но каждый символ - строковый тип
    print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3
    print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
    print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё должно работать
except TypeError:
    print('Что то пошло не так')
