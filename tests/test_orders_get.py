import allure
import pytest
from data import Common, Orders
from helpers import *


class TestOrdersGet:
    @allure.title('Тест получения списка заказов')
    def test_get_orders_list_success(self, orders_api):
        response = orders_api.get_all()
        assert is_expected_code_and_type(response, *Orders.OK_ORDERS_LIST)

    @allure.title('Тест получения заказа по трек-номеру')
    def test_get_order_by_track_number_success(self, orders_api, run_order_test):
        response, order_data = orders_api.get_order(run_order_test)
        assert (is_expected_code_and_type(response, *Orders.OK_GOT_ORDER) and
                run_order_test == order_data['track'])

    @allure.title('Тест получения заказа без трек-номера или по неверному трек-номеру')
    @pytest.mark.parametrize('track, expected',
                             [(None, Orders.ERR_INCORRECT_DATA), (Common.WRONG_ID, Orders.ERR_ORDER_NOT_FOUND)])
    def test_get_order_by_incorrect_track_number_shows_error(self, orders_api, track, expected):
        response, _ = orders_api.get_order(track)
        assert is_expected_response(response, *expected)
