import unittest

from src.vacancy import Vacancy
from src.vacancy_saver import VacancyHandler


class TestVacancyHandler(unittest.TestCase):
    def setUp(self):
        # Подготовка данных для тестов
        self.vacancy_info = [
            {'vacancy_title': 'Title 1', 'salary_from': 50000, 'salary_to': 70000},
            {'vacancy_title': 'Title 2', 'salary_from': 60000, 'salary_to': 80000},
        ]
        # Создаем экземпляры класса Vacancy из данных
        self.vacancies = [Vacancy(info) for info in self.vacancy_info]

    def test_init(self):
        # Тест инициализации VacancyHandler
        handler = VacancyHandler(self.vacancies)
        self.assertEqual(len(handler.vacancies_list), len(self.vacancy_info))

    def test_remove_without_salary(self):
        # Тест удаления вакансий без зарплаты
        handler = VacancyHandler(self.vacancies)
        handler.vacancies_list.append(Vacancy({'vacancy_title': 'Title 3', 'salary_from': 0, 'salary_to': 0}))
        handler.remove_without_salary()
        self.assertEqual(len(handler.vacancies_list), len(self.vacancies))

    def test_sort_vacancies_by_salary(self):
        # Тест сортировки вакансий по зарплате
        handler = VacancyHandler(self.vacancies)
        sorted_vacancies = handler.sort_vacancies_by_salary()
        self.assertEqual(sorted_vacancies[0].vacancy_title, 'Title 2')

    def test_search_instances_by_keywords(self):
        # Тест поиска вакансий по ключевым словам
        handler = VacancyHandler(self.vacancies)
        matching_instances = handler.search_instances_by_keywords(self.vacancies, ['Title 1'])
        self.assertEqual(len(matching_instances), 1)
