Программа получает информацию о вакансиях с популярных платформ вакансий в России 

## Как происходит взаимодействие с программой?
1. Программа запрашивает базовое слово или комбинацию слов для поиска вакансий.
2. Программа запрашивает количество вакансий.
3. Программа получает вакансии с сайта и записывает их в файл JSON. Для пользователя выводится информация о платформах 
   и общем количестве полученных вакансий.
4. Пользователю предоставляется возможность удалить из файла вакансии без указания зарплаты.
5. Пользователю предоставляется возможность вывести в консоль топ N вакансий по зарплате.
6. Пользователь может ввести дополнительные ключевые слова для фильтрации в топе вакансий 
   (будут показаны все вакансии, где содержится хотя бы одно из введённых слов).
7. Пользователь может просмотреть или записать отфильтрованные вакансии.
8. Если пользователь не ввёл слова для фильтрации, ему будет предложено сохранить в файл топ вакансий. 
   После сохранения будет выведен путь, где лежит сохранённый файл с вакансиями.
9. В конце работы программа очищает JSON-файл с вакансиями и выводит сообщение об этом.


## Какие поля существуют у вакансий?
Для единообразного отображения программа получает определённую информацию с каждого сайта:
- наименование вакансии
- регион/город
- ссылка на вакансию
- нижний уровень зарплаты
- верхний уровень зарплаты
- валюта зарплаты
- требуемый опыт работы
- требования к вакансии

Реализован метод подсчёта средней зарплаты по верхнему и нижнему уровню, 
а также возможность сравнить средние зарплаты двух вакансий 
(в программе при выводе топ N будет выведен разброс между средним самой высокооплачиваемой и 
самой низкооплачиваемой вакансии). 

### Дополнительная техническая информация:
- Максимальное количество вакансий, а также папки для хранения файлов JSON и пользовательских файлов 
  хранятся в файле config.py в корне проекта.
- Для работы со списком экземпляров класса Vacancy был создан специальный класс VacancyHandler, 
  наследующийся от Vacancy. 
- Написал тесты