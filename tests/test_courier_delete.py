import allure
import pytest

from data import Common, Courier
from helpers import *


class TestCourierDelete:

    @allure.title('Тест удаления аккаунта курьера')
    def test_delete_courier_success(self, courier_api, create_courier_data):
        _, account_id = courier_api.login(create_courier_data)
        response = courier_api.delete(account_id)
        assert is_expected_response(response, *Common.OK)

    @allure.title('Тест удаления курьера с несуществующим id или без id')
    @pytest.mark.parametrize('account_id, expected',
                             [pytest.param(Common.WRONG_ID, Courier.ERR_NO_ID, id='wrong id'),
                              pytest.param('', Common.NOT_FOUND, id='empty id')])
    def test_delete_courier_incorrect_id_shows_error(self, courier_api, account_id, expected):
        response = courier_api.delete(account_id)
        assert is_expected_response(response, *expected)
