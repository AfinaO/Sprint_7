import allure
import pytest

from data import Orders
from helpers import *


class TestOrdersCreate:

    @allure.title('Тест создания заказа с использованием разных значений поля "Цвет"')
    @pytest.mark.parametrize('color', Orders.COLORS)
    def test_create_order_with_color_success(self, orders_api, color):
        order_data = Orders.ORDER_DATA.copy()
        order_data['color'] = color
        response, track = orders_api.create(order_data)
        orders_api.cancel(track)
        assert is_expected_code_and_type(response, *Orders.OK_CREATED)
