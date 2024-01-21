import requests
from abstract.abstract_api import VacancyByAPI


class HeadHunterAPI(VacancyByAPI):
    """Класс для работы с API HeadHunter"""

    def __init__(self, vacancy_area=113, page=0, per_page=1) -> None:
        """
        Инициализатор экземпляров класса для работы с API
        :param vacancy_area: область поиска -- по умолчанию по всей России
        :param page: страница поиска -- по умолчанию 0 (начальная)
        :param per_page: количество вакансий на страницу -- по умолчанию 50
        """
        self.vacancy_area = vacancy_area
        self.page = page
        self.per_page = per_page

    def get_vacancy(self, vacancy_title: str, url="https://api.hh.ru/vacancies") -> list[str] or list:
        """
        :param url: Сайт для API
        :param vacancy_title: Название профессии
        :return: Список вакансий для создания экземпляров класса Vacancy
        """
        params = {
            'text': vacancy_title,
            'area': self.vacancy_area,
            'page': self.page,
            'per_page': self.per_page
        }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            vacancies = response.json()['items']

            if vacancies:
                list_vacancies = self.__class__.organizator(vacancies)
                return list_vacancies
            return []
        else:
            print(f"Ошибка {response.status_code} при обработке запроса")
            return []

    @staticmethod
    def organizator(vacancy_data: list) -> list:
        """
        Организует данные по вакансиям
        :param vacancy_data: список профессий из API
        :return: Сортированный список вакансий
        """
        organizator_list = []
        for vacancy in vacancy_data:
            vacancy_title = vacancy.get('name')
            vacancy_area = vacancy.get('area')['name']
            vacancy_url = f"https://hh.ru/vacancy/{vacancy.get('id')}"
            salary = vacancy.get('salary')
            if not salary:
                salary_from = 0
                salary_to = 0
                currency = ''
            else:
                salary_from = salary.get('from')
                salary_to = salary.get('to')
                if not salary_to:
                    salary_to = salary_from
                if not salary_from:
                    salary_from = salary_to
                currency = vacancy.get('salary')['currency']
            experience = vacancy.get('experience')['name']
            requirements = vacancy.get('snippet', {}).get('requirements', '')
            if requirements:
                requirements = requirements.strip().replace('<highlighttext>', '')

            vacancy_info = {
                'vacancy_title': vacancy_title,
                'vacancy_area': vacancy_area,
                'vacancy_url': vacancy_url,
                'salary_from': salary_from,
                'salary_to': salary_to,
                'currency': currency,
                'experience': experience,
                'requirements': requirements
            }

            organizator_list.append(vacancy_info)

        return organizator_list
