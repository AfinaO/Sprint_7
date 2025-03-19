import allure
import pytest

from data import Common, Courier
from helpers import *


class TestCourierCreate:

    @allure.title('Тест создания учётной записи курьера')
    def test_create_account_success(self, courier_api):
        response, account = courier_api.create(get_account_data())
        _, account_id = courier_api.login(account)
        courier_api.delete(account_id)
        assert is_expected_response(response, *Common.CREATED)

    @allure.title('Тест создания двух курьеров с одинаковым логином')
    def test_create_courier_duplicate_shows_error(self, courier_api, run_courier_test):
        response, _ = courier_api.create(run_courier_test)
        assert is_expected_response(response, *Courier.ERR_DUPLICATED)

    @allure.title('Тест создания курьера без логина или пароля')
    @pytest.mark.parametrize(
        'account', [pytest.param(Courier.LOGIN, id='login only'),
                    pytest.param(Courier.PASSWORD, id='password only')]
    )
    def test_create_courier_incorrect_data_shows_error(self, courier_api, account):
        response, _ = courier_api.create(account)
        assert is_expected_response(response, *Courier.ERR_MISS_DATA_CREATE)
