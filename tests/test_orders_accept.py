import allure
import pytest
from data import Common, Orders
from helpers import *


class TestOrdersAccept:

    @allure.title('Тест обработки заказа')
    def test_accept_order_success(self, orders_api, courier_api, run_courier_test, run_order_test):
        _, courier_id = courier_api.login(run_courier_test)
        _, order_data = orders_api.get_order(run_order_test)

        response = orders_api.accept(
            order_data.get('id'), courier_id
        )
        assert is_expected_response(response, *Common.OK)

    @allure.title('Тест обработки заказа без id курьера или с неверным id курьера')
    @pytest.mark.parametrize('courier_id, expected', [(None, Orders.ERR_INCORRECT_DATA),
                                                      (Common.WRONG_ID, Orders.ERR_INCORRECT_COURIER_ID)])
    def test_order_incorrect_courier_id_shows_error(self, orders_api, run_order_test, courier_id, expected):
        _, order_data = orders_api.get_order(run_order_test)
        response = orders_api.accept(order_data.get('id'), courier_id)
        assert is_expected_response(response, *expected)

    @allure.title('Тест обработки заказа без id заказа или с не корректным id заказа')
    @pytest.mark.parametrize('order_id, expected',
                             [(Common.WRONG_ID, Orders.ERR_INCORRECT_ORDER_ID), ('', Common.NOT_FOUND)])
    def test_order_incorrect_order_id_shows_error(self, courier_api, orders_api, run_courier_test, order_id, expected):
        _, courier_id = courier_api.login(run_courier_test)
        response = orders_api.accept(order_id, courier_id)
        assert is_expected_response(response, *expected)
