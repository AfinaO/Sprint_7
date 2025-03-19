import pytest

from api_methods import *
from data import Orders
from helpers import get_account_data


@pytest.fixture()
def courier_api():
    return CourierAPI()


@pytest.fixture()
def orders_api():
    return OrdersAPI()


@pytest.fixture()
def create_courier_data(courier_api):
    account_data = get_account_data()
    courier_api.create(account_data)
    return account_data


@pytest.fixture()
def run_courier_test(courier_api, create_courier_data):
    yield create_courier_data
    courier_api.delete(create_courier_data)


@pytest.fixture()
def run_order_test(orders_api):
    _, track = orders_api.create(Orders.ORDER_DATA)
    yield track
    orders_api.cancel(track)
