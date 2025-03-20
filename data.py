class Common:
    WRONG_ID = 0
    OK_TRUE = {'ok': True}
    CREATED = 201, OK_TRUE
    NOT_FOUND = 404, 'Not Found.'
    OK = 200, OK_TRUE


class Courier:
    LOGIN = {'login': 'Login'}
    EMPTY_PASSWORD = {'login': 'test', 'password': ''}  # без пароля - ошибка 504
    PASSWORD = {'password': 'test'}
    WRONG_ACCOUNT = {'login': 'Login', 'password': 'Test'}
    WRONG_LOGIN = {'login': '1111111'}
    WRONG_PASSWORD = {'password': '2222222'}
    ERR_DUPLICATED = 409, 'Этот логин уже используется. Попробуйте другой.'
    OK_LOGGED_IN = 200, 'id', int
    ERR_MISS_DATA_CREATE = 400, 'Недостаточно данных для создания учетной записи'
    ERR_MISS_DATA_LOGIN = 400, 'Недостаточно данных для входа'
    ERR_NOT_FOUND_ACC = 404, 'Учетная запись не найдена'
    ERR_NO_ID = 404, 'Курьера с таким id нет.'


class Orders:
    OK_CREATED = 201, 'track', int
    OK_GOT_ORDER = 200, 'order', dict
    OK_ORDERS_LIST = 200, 'orders', list
    ERR_INCORRECT_DATA = 400, 'Недостаточно данных для поиска'
    ERR_ORDER_NOT_FOUND = 404, 'Заказ не найден'
    ERR_INCORRECT_COURIER_ID = 404, 'Курьера с таким id не существует'
    ERR_INCORRECT_ORDER_ID = 404, 'Заказа с таким id не существует'
    COLORS = ['GREY'], ['BLACK'], [], ['BLACK', 'GREY']
    ORDER_DATA = {
        'firstName': 'Дональд',
        'lastName': 'Трамп',
        'address': 'Вашингтон ДС',
        'metroStation': 1,
        'phone': '1-POTUS-1',
        'rentTime': 4,
        'deliveryDate': '2028-01-12',
        'comment': 'Мейк Америка грейт эгейн!'
    }
