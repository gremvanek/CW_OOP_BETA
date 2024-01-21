import unittest
import os
from src.json_keeper import JSONKeeping
from src.vacancy import Vacancy
from config import JSON_DATA_DIR


class TestJSONKeeping(unittest.TestCase):
    def setUp(self):
        # Подготовка данных для тестов
        self.filename = 'test_vacancies.json'
        self.full_filename = os.path.join(JSON_DATA_DIR, self.filename)
        self.vacancy_list = [
            {'vacancy_title': 'Title 1', 'salary_from': 50000, 'salary_to': 70000},
            {'vacancy_title': 'Title 2', 'salary_from': 60000, 'salary_to': 80000},
            {'vacancy_title': 'Title 3', 'salary_from': 0, 'salary_to': 0},
        ]
        self.instances = [Vacancy(info) for info in self.vacancy_list]

    def tearDown(self):
        # Очистка данных после тестов
        if os.path.exists(self.full_filename):
            os.remove(self.full_filename)

    def test_save_load_vacancies(self):
        # Тест сохранения и загрузки вакансий в/из JSON-файла
        json_keeper = JSONKeeping(self.filename)
        json_keeper.save_vacancies_to_json(self.vacancy_list)
        loaded_data = json_keeper.load_vacancies()
        self.assertEqual(loaded_data, self.vacancy_list)

    def test_remove_zero_salary_vacancies(self):
        # Тест удаления вакансий с нулевой зарплатой
        json_keeper = JSONKeeping(self.filename)
        json_keeper.save_vacancies_to_json(self.vacancy_list)
        json_keeper.remove_zero_salary_vacancies()
        loaded_data = json_keeper.load_vacancies()
        self.assertEqual(len(loaded_data), 2)
        self.assertNotIn({'vacancy_title': 'Title 3', 'salary_from': 0, 'salary_to': 0}, loaded_data)

    def test_json_to_instances(self):
        # Тест преобразования JSON-данных в экземпляры класса
        json_keeper = JSONKeeping(self.filename)
        json_keeper.save_vacancies_to_json(self.vacancy_list)
        instances = json_keeper.json_to_instances(Vacancy)
        # Проверяем, что количество экземпляров совпадает
        self.assertEqual(len(instances), len(self.instances))
        for actual_instance, expected_instance in zip(instances, self.instances):
            self.assertEqual(actual_instance.__dict__, expected_instance.__dict__)

    def test_clear_json_with_vacancies(self):
        # Тест очистки JSON-файла
        json_keeper = JSONKeeping(self.filename)
        json_keeper.save_vacancies_to_json(self.vacancy_list)
        json_keeper.clear_json_with_vacancies()
        self.assertTrue(os.path.exists(self.full_filename))


if __name__ == '__main__':
    unittest.main()
