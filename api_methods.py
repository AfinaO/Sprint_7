import allure
import requests
import json

from config import *


class CourierAPI:

    @allure.step('Создаем курьера.')
    def create(self, account_data):
        return requests.post(url=API_COURIER, data=account_data), account_data

    @allure.step('Авторизуем курьера.')
    def login(self, account_data):
        response = requests.post(url=API_COURIER_LOGIN, data=account_data)
        return response, response.json().get('id')

    @allure.step('Удаляем курьера.')
    def delete(self, account_id):
        return requests.delete(url=API_COURIER_DELETE.format(id=account_id))


class OrdersAPI:

    @allure.step('Создаем заказ.')
    def create(self, order_data):
        response = requests.post(url=API_ORDERS, data=json.dumps(order_data))
        return response, response.json().get('track')

    @allure.step('Отменяем заказ.')
    def cancel(self, track):
        return requests.put(url=API_ORDERS_CANCEL, data={'track': track})

    @allure.step('Полученаем все заказы.')
    def get_all(self):
        return requests.get(url=API_ORDERS)

    @allure.step('Получаем заказы по трек-номеру.')
    def get_order(self, track):
        response = requests.get(url=API_ORDERS_GET, params={'t': track})
        order_data = response.json().get('order')
        return response, order_data

    @allure.step('Прием заказа курьером.')
    def accept(self, order_id, courier_id):
        return requests.put(url=API_ORDERS_ACCEPT.format(id=order_id), params={'courierId': courier_id})
