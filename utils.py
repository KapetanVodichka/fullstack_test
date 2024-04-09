def unique_elements(int_list: list[int]) -> list:
    """ Принимает список целых чисел, возвращает список уникальных значений """
    return list(set(int_list))


def simple_nums(min_num: int, max_num: int) -> list:
    """ Принимает 2 целых числа и в диапазоне этих чисел возвращает список простых чисел """
    return [x for x in range(min_num, max_num + 1) if all(x % i != 0 for i in range(2, x))]


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to_point(self, point):
        return ((self.x - point.x) ** 2 + (self.y - point.y) ** 2) ** 0.5

    def get_position(self):
        return self.x, self.y

    def set_position(self, x, y):
        self.x = x
        self.y = y


# функции для 4 задания
def sorting_asc(string: list[str]) -> list[str]:
    """ Сортировка по длине (возрастание) """
    sorted_asc = sorted(string, key=len)
    return sorted_asc


def sorting_desc(string: list[str]) -> list[str]:
    """ Сортировка по длине (убывание) """
    sorted_desc = sorted(string, key=len, reverse=True)
    return sorted_desc
