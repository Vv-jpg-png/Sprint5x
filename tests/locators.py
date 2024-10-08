#
# Переменные для входной панели
#

LOGIN_EMAIL_XPATH    = '//input[@class="text input__textfield text_type_main-default" and @type="text"]'
LOGIN_PASSWORD_XPATH = '//input[@class="text input__textfield text_type_main-default" and @type="password"]'

#
# Переменные для входа: Вход, Вход (ждать) в аккаунт(через основную панель)
#

LOGIN_BUTTON_XPATH            = '//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"]'
LOGIN_BUTTON_WAIT_XPATH       = LOGIN_BUTTON_XPATH
LOGIN_NORMAL_INPUT_WAIT_XPATH = '//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg"]'
LOGIN_NORMAL_INPUT_XPATH      = LOGIN_NORMAL_INPUT_WAIT_XPATH

#
# Переменные для входа в кабинет и регистрации
#
REGISTER_A_XPATH = '//p/a[@href="/login"]'
#
# Переменные для забытого пароля
#
FORGET_A_XPATH = "//a[@href='/forgot-password']"

LOGIN_EMAIL_FORGET_XPATH        = '//input[@type="text" and @name="name"]'
LOGIN_EMAIL_FORGET_BUTTON_XPATH = '//form/button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"]'

LOGIN_PASSWORD_FORGET_XPATH    = "//fieldset[1]/div/div/input[@type='password']"
LOGIN_LETTER_CODE_FORGET_XPATH = "//fieldset[2]/div/div/input[@type='text']"
LOGIN_FORGET_BUTTON            = "//form/button[text()='Сохранить']"

#
# Переменные для регистрации
#

REGISTRATION_NAME_XPATH  = '//form/fieldset[1]/div/div/input[@class="text input__textfield text_type_main-default" and @type="text"]'
REGISTRATION_EMAIL_XPATH = '//form/fieldset[2]/div/div/input[@class="text input__textfield text_type_main-default" and @type="text"]'
REGISTRATION_PASSWORD_XPATH = '//form/fieldset[3]/div/div/input[@class="text input__textfield text_type_main-default" and @type="password"]'
REGISTRATION_BUTTON_XPATH = '//form/button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"]'

#
# Переменные для отработки неправильного пароля
#

LOGIN_WRONG_ACCOUNT_WAIT_XPATH = "//fieldset[2]/div/p[@class='input__error text_type_main-default']"
LOGIN_WRONG_ACCOUNT_XPATH      = "//fieldset[2]/div/p"

#
# Переменные для работы с кабинетом: вход, выходная кнопка, ссылка на конструктор, ссылка на логотип
#
CABINET_A_XPATH = '//a[@href="/account"]'

CABINET_EXIT_BUTTON_XPATH   = '//ul/li/button[@class="Account_button__14Yp3 text text_type_main-medium text_color_inactive"]'
CABINET_CONSTRUCTOR_A_XPATH = '//a[@class="AppHeader_header__link__3D_hX"]'
CABINET_LOGOTYPE_A_XPATH    = "//a[@href='/']"

CABINET_LOGIN_BUTTON_XPATH = '//button[text()="Войти"]'

#
# Переменные для рааботы с подменю Булки, Соусы, Начинки
#

CONSTR_BULKI_WAIT_XPATH = '//main/section[1]/div[1]/div[1]/span'
#CONSTR_BULKI_A_XPATH    = '//main/section[1]/div[1]' # ?????
CONSTR_BULKI_A_XPATH    = '//parent::div'
CONSTR_SOUGE_A_XPATH    = '//main/section[1]/div[1]/div[2]/span'
CONSTR_NACHINKA_A_XPATH = '//main/section[1]/div[1]/div[3]/span'

CONSTR_BULKI_ASSERT     = '//main/section[1]/div[1]/div[1]'
CONSTR_SOUGE_ASSERT     = '//main/section[1]/div[1]/div[2]'
CONSTR_NACHINKA_ASSERT  = '//main/section[1]/div[1]/div[3]'

#
# Переменные для рааботы с успешным входом
#
LOGIN_SUCCESS_WAIT_XPATH = '//button[text()="Оформить заказ"]'
LOGIN_SUCCESS_XPATH      = '//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg"]'
LOGIN_SUCCESS_WAIT_XPATH = LOGIN_SUCCESS_XPATH

#URLs

URL_COMMON = 'https://stellarburgers.nomoreparties.site'
URL_LOGIN = 'https://stellarburgers.nomoreparties.site/login'
URL_REGISTRATION = 'https://stellarburgers.nomoreparties.site/register'