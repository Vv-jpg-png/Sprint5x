# Sprint5

2024-08-29

Описание проекта:

Проект выполнен на selenium на ubuntu.
Для уверенности я использовал один-два pip

pip install selenium

Сейчас видимость включена, то есть при выполнении тестов, браузер будет виден.

Все тесты организованны в 4 тест-файлах и conftest.py, который содержит фикстуры.

Файлы:

    TestRegistration.py тест-проверка регистрации положительной и отрицательной
    TestAccount.py      тест-проверка входа с аккоунтом положительной и отрицательной
            Вход по кнопке Войти на главной
            Вход в Личный кабинет
            Вход через регистрацию
            Вход через воссттановление пароля
            Отрицательный тест на вход
    TestCabinetMy.py    тест-проверка моего кабинета положительной и отрицательной
            Переход в личный кабинет
            Переход в конструктор из кабинета
            Переход на логотип 
            Выход из кабинета через клавишу Выход
    TestConstructor.py  тест-проверка переходов в конструкторе положительной
            Переходы на Булки
            Переходы на Соусы
            Переходы на Начинки

