from abc import ABC, abstractmethod


class VacancyByAPI(ABC):
    """
    Абстрактный класс для работы с апи по ТЗ курсовой
    """

    @abstractmethod
    def get_vacancy(self, vacancy_title: str) -> list:
        """
        Получение списка вакансий
        :param vacancy_title: Название профессии
        :return: список с необходимыми данными
        """
        pass

    @staticmethod
    @abstractmethod
    def organizator(vacancy_data: list) -> list:
        """
        Формирует список вакансий в необходимом виде
        :param vacancy_data: Информация по выбранной профессии
        :return: Список в организованном виде
        """
        pass
