#
# Переменные для входной панели
#

LOGIN_EMAIL = '#root > div > main > div > form > fieldset:nth-child(1) > div > div > input'
LOGIN_PASSWORD = '#root > div > main > div > form > fieldset:nth-child(2) > div > div > input'
LOGIN_BUTTON = '#root > div > main > div > form > button'

#
# Переменные для входа: Вход, Вход (ждать) в аккаунт(через основную панель)
#

LOGIN_BUTTON_WAIT_XPATH       = '//*[@id="root"]/div/main/div/form/button[text()="Войти"]'
LOGIN_NORMAL_INPUT_WAIT_XPATH = '//*[@id="root"]/div/main/section[2]/div/button[text()="Войти в аккаунт"]'
LOGIN_NORMAL_INPUT_XPATH      = '//*[@id="root"]/div/main/section[2]/div/button'

#
# Переменные для входа в кабинет и регистрации
#

CABINET_A = '#root > div > header > nav > a'
A_REGISTRATION = '#root > div > main > div > div > p > a'

#
# Переменные для забытого пароля
#

A_FORGET = '#root > div > main > div > div > p:nth-child(2) > a'

LOGIN_EMAIL_FORGET_XPATH = '//*[@id="root"]/div/main/div/form/fieldset/div/div/input'
LOGIN_EMAIL_FORGET_BUTTON_XPATH = '//*[@id="root"]/div/main/div/form/button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"]'

LOGIN_PASSWORD_FORGET_XPATH = "//*[@id='root']/div/main/div/form/fieldset[1]/div/div/input[@type='password']"
LOGIN_LETTER_CODE_FORGET_XPATH = "/html/body/div/div/main/div/form/fieldset[2]/div/div/input[@type='text']"
LOGIN_FORGET_BUTTON = "//*[@id='root']/div/main/div/form/button[text()='Сохранить']"

#
# Переменные для регистрации
#

REGISTRATION_NAME = '#root > div > main > div > form > fieldset:nth-child(1) > div > div > input'
REGISTRATION_EMAIL = '#root > div > main > div > form > fieldset:nth-child(2) > div > div > input'
REGISTRATION_PASSWORD = '#root > div > main > div > form > fieldset:nth-child(3) > div > div > input'
REGISTRATION_BUTTON = '#root > div > main > div > form > button'

#
# Переменные для отработки неправильного пароля
#

LOGIN_WRONG_ACCOUNT_WAIT_XPATH = "//*[@id='root']/div/main/div/form/fieldset[2]/div/p[@class='input__error text_type_main-default']"
LOGIN_WRONG_ACCOUNT_XPATH = "//*[@id='root']/div/main/div/form/fieldset[2]/div/p"

#
# Переменные для работы с кабинетом: вход, выходная кнопка, ссылка на конструктор, ссылка на логотип
#

CABINET_A_XPATH = '//*[@id="root"]/div/header/nav/a'
CABINET_EXIT_BUTTON_XPATH = "//*[@id='root']/div/main/div/nav/ul/li[3]/button"
CABINET_CONSTRUCTOR_A_XPATH = "//*[@id='root']/div/header/nav/ul/li[1]/a"
CABINET_LOGOTYPE_A_XPATH = "//*[@id='root']/div/header/nav/div/a"

CABINET_LOGIN_BUTTON_XPATH = '//*[@id="root"]/div/main/div/form/button[text()="Войти"]'

#
# Переменные для рааботы с подменю Булки, Соусы, Начинки
#

CONSTR_BULKI_WAIT_XPATH = '//*[@id="root"]/div/main/section[1]/div[1]/div[1]/span'
CONSTR_BULKI_A_XPATH    = '//*[@id="root"]/div/main/section[1]/div[1]'
CONSTR_SOUGE_A_XPATH    = '//*[@id="root"]/div/main/section[1]/div[1]/div[2]/span'
CONSTR_NACHINKA_A_XPATH = '//*[@id="root"]/div/main/section[1]/div[1]/div[3]/span'

#
# Переменные для рааботы с успешным входом
#
LOGIN_SUCCESS_WAIT_XPATH = '//*[@id="root"]/div/main/section[2]/div/button[text()="Оформить заказ"]'
LOGIN_SUCCESS_XPATH      = '//*[@id="root"]/div/main/section[2]/div/button'

