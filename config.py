API_MAIN = 'https://qa-scooter.praktikum-services.ru/api/v1/'

API_COURIER = API_MAIN + 'courier/'
API_COURIER_DELETE = API_COURIER + '{id}'
API_COURIER_LOGIN = API_COURIER + 'login/'

API_ORDERS = API_MAIN + 'orders'
API_ORDERS_ACCEPT = API_ORDERS + '/accept/{id}'
API_ORDERS_CANCEL = API_ORDERS + '/cancel'
API_ORDERS_GET = API_ORDERS + '/track'
