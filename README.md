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

Локаторы:

    Email(login)    By.CSS_SELECTOR,'#root > div > main > div > form > fieldset:nth-child(1) > div > div > input' 
    Password(login) By.CSS_SELECTOR,'#root > div > main > div > form > fieldset:nth-child(2) > div > div > input'
    Войти(login)    By.CSS_SELECTOR, '#root > div > main > div > form > button'

    Личный кабинет  By.CSS_SELECTOR,'#root > div > header > nav > a'

    Регистрация     By.CSS_SELECTOR,'#root > div > main > div > div > p > a'

    Кнопка Зарегистрировать    By.CSS_SELECTOR, '#root > div > main > div > form > button'

    Восстановление паролей
        Кнопка Восстановить пароль By.CSS_SELECTOR,'#root > div > main > div > div > p:nth-child(2) > a'
        Поле для email                      By.XPATH,'//*[@id="root"]/div/main/div/form/fieldset/div/div/input'
        Кнопка послать код для восстановления By.XPATH,'//*[@id="root"]/div/main/div/form/button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"]'
        Пароль для восстановления           By.XPATH,"//*[@id='root']/div/main/div/form/fieldset[1]/div/div/input[@type='password']"
        Код из письма для восстановления    By.XPATH, "/html/body/div/div/main/div/form/fieldset[2]/div/div/input[@type='text']"
        Кнопка Сохранить                    By.XPATH, "//*[@id='root']/div/main/div/form/button[text()='Сохранить']"

    Регистрация
      Имя      By.CSS_SELECTOR,'#root > div > main > div > form > fieldset:nth-child(1) > div > div > input'
      Email    By.CSS_SELECTOR,'#root > div > main > div > form > fieldset:nth-child(2) > div > div > input'
      Password By.CSS_SELECTOR,'#root > div > main > div > form > fieldset:nth-child(3) > div > div > input'
      Кнопка Регистрация By.CSS_SELECTOR,'#root > div > main > div > form > button'

    Поле Некоректный пароль By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[2]/div/p"

    Кнопка Личный кабинет          By.XPATH,'//*[@id="root"]/div/header/nav/a'
    Кнопка Конструктор из кабинета By.XPATH,"//*[@id='root']/div/header/nav/ul/li[1]/a"
    Кнопка Логотипа из кабинета    By.XPATH,"//*[@id='root']/div/header/nav/div/a"
    Кнопка Выход из кабинета       By.XPATH,"//*[@id='root']/div/main/div/nav/ul/li[3]/button"

    Переход на Булки из конструктора   By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]'
    Переход на Соусы из конструктора   By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[2]/span'
    Переход на Начинки из конструктора By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[3]/span'

