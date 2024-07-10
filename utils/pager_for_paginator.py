from typing import List


class Pager:
    """
    Класс используется как хранилище списка с внешним доступом для пагинатора.
    """

    def __init__(self):
        self._my_strings = None

    @property
    def my_strings(self) -> List[str]:
        """
        Геттер для списка. Используется в пагинаторе.

        :return: _my_strings
        :rtype: List[str]
        """
        return self._my_strings

    @my_strings.setter
    def my_strings(self, val: List[str]) -> None:
        """
        Сеттер для списка. Используется извне для записи списка.

        :param val: Список строк с информацией.
        :type val: List[str]
        """
        self._my_strings = val


my_pages = Pager()
